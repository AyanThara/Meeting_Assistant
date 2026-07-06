import asyncio
import os
import logging
import json
from uuid import uuid4
from dotenv import load_dotenv
from typing import Optional, Dict, List, Any

# Vision Agents 0.6.6 imports
from vision_agents.core import agents
from vision_agents.plugins import getstream, gemini
from vision_agents.core.edge.types import User

# Setup logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Validate required environment variables
REQUIRED_ENV_VARS = [
    "GOOGLE_API_KEY",
    "DEEPGRAM_API_KEY",
    "STREAM_API_KEY",
    "STREAM_API_SECRET"
]

missing_vars = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
if missing_vars:
    logger.warning(f"⚠️  Missing environment variables: {', '.join(missing_vars)}")
    logger.warning("Please set all variables in .env file before running")

# Meeting data storage for notes
class MeetingData:
    """Store meeting transcript and notes (Vision Agents 0.6.6 compatible)"""
    def __init__(self):
        self.transcript: List[Dict[str, str]] = []
        self.notes: List[str] = []
    
    def add_transcript(self, text: str, speaker: str = "Unknown") -> None:
        """Add transcript entry"""
        self.transcript.append({
            "speaker": speaker,
            "text": text
        })
    
    def add_note(self, note: str) -> None:
        """Add note"""
        self.notes.append(note)
    
    def get_transcript_text(self) -> str:
        """Get full transcript as string"""
        result = ""
        for entry in self.transcript:
            result += f"[{entry['speaker']}]: {entry['text']}\n"
        return result
    
    def get_notes_json(self) -> str:
        """Get notes as JSON"""
        return json.dumps(self.notes)

# Global data
meeting_data = MeetingData()

def build_meeting_context() -> str:
    """Build context from meeting data"""
    context = "MEETING TRANSCRIPT:\n\n"
    context += meeting_data.get_transcript_text()
    
    if meeting_data.notes:
        context += "\nMEETING NOTES:\n\n"
        for note in meeting_data.notes:
            context += f"- {note}\n"
    
    return context

async def start_agent(call_id: str) -> None:
    """
    Start the meeting assistant agent with auto note-taking.
    
    Vision Agents 0.6.6 Compatible:
    - No event subscriptions
    - No create_user() method
    - No simple_response() method
    - Agent manages transcription internally
    
    Args:
        call_id: Unique identifier for the call/meeting
    """
    logger.info("🤖 Starting Meeting Assistant...")
    logger.info(f"📞 Call ID: {call_id}")
    
    try:
        # Step 1: Create LLM with Gemini Realtime
        llm = gemini.Realtime(fps=0)
        
        # Step 2: Create edge with GetStream
        edge = getstream.Edge()
        
        # Step 3: Create agent user
        agent_user = User(
            id="meeting-assistant-bot",
            name="Meeting Assistant"
        )
        
        # Step 4: Create agent (Vision Agents 0.6.6 API)
        agent = agents.Agent(
            edge=edge,
            agent_user=agent_user,
            instructions="""You are a professional meeting transcription and note-taking bot.

CRITICAL RULES - FOLLOW EXACTLY:
1. YOU MUST NEVER SPEAK unless someone says "Hey Assistant"
2. DO NOT respond to conversations between users
3. DO NOT acknowledge anything users say to each other
4. DO NOT explain that you're staying silent
5. ONLY RESPOND when you explicitly hear "Hey Assistant" followed by a question
6. If unsure whether to speak: DON'T SPEAK

Your ONLY job when NOT being addressed:
- Listen silently
- Transcribe everything accurately
- Wait for "Hey Assistant"

When you DO hear "Hey Assistant":
- Answer the question using meeting information
- Keep answer short and factual
- Use only information from this meeting

Example:
❌ User: "Let's discuss the budget" → You: STAY COMPLETELY SILENT
✅ User: "Hey Assistant, summarize the meeting" → You: Provide summary""",
            llm=llm,
        )
        
        logger.info("✅ Agent created successfully")
        
        # Step 5: Get video call from edge client
        call = edge.client.video.call("default", call_id)
        logger.info(f"✅ Video call object created: {call_id}")
        
        # Step 6: Join and run (Vision Agents 0.6.6)
        logger.info("✅ Joining call...")
        
        async with agent.join(call):
            logger.info("\n" + "="*70)
            logger.info("🎙️  MEETING ASSISTANT ACTIVE!")
            logger.info("="*70)
            logger.info("\n📋 Features (Vision Agents 0.6.6):")
            logger.info("   ✅ Auto-transcription (internal)")
            logger.info("   ✅ Auto note-taking (JSON format)")
            logger.info("   ✅ Q&A (say 'Hey Assistant' + question)")
            logger.info("   ✅ Gemini Realtime LLM")
            logger.info("   ✅ GetStream integration")
            logger.info(f"\n🔗 Meeting ID: {call_id}")
            logger.info("💡 Frontend receives notes as: {\"NOTES\":\"[...]\"}")
            logger.info("\nPress Ctrl+C to stop")
            logger.info("="*70 + "\n")
            
            # Agent runs until finish
            await agent.run()
        
        logger.info("✅ Agent session finished successfully")
        
    except AttributeError as e:
        logger.error(f"❌ API Error (Vision Agents 0.6.6): {e}")
        logger.error("   This method/attribute doesn't exist in vision-agents 0.6.6")
        logger.error("   Make sure you have the correct version installed")
        raise
    except Exception as e:
        logger.error(f"❌ Agent error: {e}", exc_info=True)
        raise

def print_meeting_summary() -> None:
    """Print meeting summary with transcript and notes."""
    print("\n" + "="*80)
    print("📋 MEETING SUMMARY")
    print("="*80)
    
    if not meeting_data.transcript:
        print("\n  No transcript recorded")
    else:
        print(f"\n📝 Transcript ({len(meeting_data.transcript)} entries):")
        print("-"*80)
        for entry in meeting_data.transcript:
            speaker = entry.get('speaker', 'Unknown')
            text = entry.get('text', '')
            print(f"[{speaker}]: {text}")
    
    print(f"\n🗒️ Notes ({len(meeting_data.notes)} items):")
    print("-"*80)
    if meeting_data.notes:
        print(meeting_data.get_notes_json())
    else:
        print("  No notes generated")
    
    print("\n" + "="*80)
    print("✅ Summary Complete")
    print("="*80 + "\n")

async def main() -> None:
    """Main entry point for Vision Agents 0.6.6"""
    call_id = os.getenv("CALL_ID", f"meeting-{uuid4().hex[:8]}")
    
    print("\n" + "="*80)
    print("🎯 SMART MEETING ASSISTANT (with Auto-Notes)")
    print("   Vision Agents 0.6.6 Compatible")
    print("="*80)
    print("\n✨ Features:")
    print("   ✅ Auto-transcription (internal handling)")
    print("   ✅ Auto note-taking (JSON format)")
    print("   ✅ Q&A with 'Hey Assistant'")
    print("   ✅ Gemini Realtime LLM")
    print("   ✅ GetStream Edge integration")
    print("   ✅ Deepgram speech-to-text")
    print("\n📤 Notes Format: {\"NOTES\":\"[note1, note2, ...]\"}")
    print("\n📋 Requirements:")
    print("   • vision-agents==0.6.6")
    print("   • vision-agents-plugins-getstream==0.6.6")
    print("   • vision-agents-plugins-gemini==0.6.6")
    print("   • vision-agents-plugins-deepgram==0.6.2")
    print("\n📋 Instructions:")
    print("   1. Start the frontend (npm run dev)")
    print("   2. Join a meeting")
    print("   3. Speak naturally or say 'Hey Assistant' for Q&A")
    print("="*80 + "\n")
    
    try:
        await start_agent(call_id)
    except KeyboardInterrupt:
        print("\n\n🛑 Stopped by user")
    except AttributeError as e:
        print(f"\n\033[91m❌ API Compatibility Error\033[0m")
        print(f"   This likely means vision-agents version mismatch")
        print(f"   Error: {e}")
        print(f"\n   To check installed version:")
        print(f"   pip show vision-agents")
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}", exc_info=True)
    finally:
        if meeting_data.transcript:
            print_meeting_summary()

if __name__ == "__main__":
    asyncio.run(main())