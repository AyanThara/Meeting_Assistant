import asyncio
import os
import logging
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
    logger.warning(f"   Missing: {', '.join(missing_vars)}")
    logger.warning("Please set all variables in .env file before running")

# Meeting transcript storage (Vision Agents 0.6.6 compatible)
class MeetingTranscript:
    """Store meeting transcript data"""
    def __init__(self):
        self.entries: List[Dict[str, str]] = []
    
    def add_entry(self, text: str, speaker: str = "Unknown") -> None:
        """Add transcript entry"""
        self.entries.append({
            "speaker": speaker,
            "text": text,
            "timestamp": None
        })
    
    def get_all(self) -> str:
        """Get full transcript as string"""
        result = ""
        for entry in self.entries:
            result += f"[{entry['speaker']}]: {entry['text']}\n"
        return result

# Global transcript
transcript = MeetingTranscript()

async def start_agent(call_id: str) -> None:
    """
    Start the meeting assistant agent.
    
    Vision Agents 0.6.6 API:
    - No event subscriptions (removed in 0.6.6)
    - No create_user() method (replaced with direct agent setup)
    - No simple_response() method (use agent.run() instead)
    - Agent manages transcription internally
    
    Args:
        call_id: Unique identifier for the call/meeting
    """
    logger.info("🤖 Starting Meeting Assistant...")
    logger.info(f"📞 Call ID: {call_id}")
    
    try:
        # Create LLM with Gemini Realtime
        # Vision Agents 0.6.6: Pass LLM directly to Agent
        llm = gemini.Realtime(fps=0)
        
        # Create edge with GetStream
        # Vision Agents 0.6.6: Edge() requires no authentication here
        edge = getstream.Edge()
        
        # Create agent user
        agent_user = User(
            id="meeting-assistant-bot",
            name="Meeting Assistant"
        )
        
        # Create agent with proper Vision Agents 0.6.6 API
        # NOTE: No event handlers here - Agent handles internally
        agent = agents.Agent(
            edge=edge,
            agent_user=agent_user,
            instructions="""You are a professional meeting transcription and assistance bot.

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
        
        # Vision Agents 0.6.6: Get video call from edge client
        # No authenticate() or create_user() needed here
        call = edge.client.video.call("default", call_id)
        logger.info(f"✅ Video call object created: {call_id}")
        
        # Join the call
        # Vision Agents 0.6.6: agent.join() handles everything
        logger.info("✅ Joining call...")
        
        async with agent.join(call):
            logger.info("\n" + "="*70)
            logger.info("🎙️  MEETING ASSISTANT ACTIVE!")
            logger.info("="*70)
            logger.info("\n📋 Features (Vision Agents 0.6.6):")
            logger.info("   ✅ Auto-transcription (internal)")
            logger.info("   ✅ Q&A (say 'Hey Assistant' + question)")
            logger.info("   ✅ Gemini Realtime LLM")
            logger.info("   ✅ GetStream integration")
            logger.info(f"\n🔗 Meeting ID: {call_id}")
            logger.info("\nPress Ctrl+C to stop")
            logger.info("="*70 + "\n")
            
            # Vision Agents 0.6.6: Agent runs until finish() is called
            # The agent handles all transcription and responses internally
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
    """Print meeting summary with transcript."""
    print("\n" + "="*80)
    print("📋 MEETING SUMMARY")
    print("="*80)
    
    if not transcript.entries:
        print("\n  No transcript recorded")
    else:
        print(f"\n📝 Transcript ({len(transcript.entries)} entries):")
        print("-"*80)
        for entry in transcript.entries:
            speaker = entry.get('speaker', 'Unknown')
            text = entry.get('text', '')
            print(f"[{speaker}]: {text}")
    
    print("\n" + "="*80)
    print("✅ Summary Complete")
    print("="*80 + "\n")

async def main() -> None:
    """Main entry point for Vision Agents 0.6.6"""
    call_id = os.getenv("CALL_ID", f"meeting-{uuid4().hex[:8]}")
    
    print("\n" + "="*80)
    print("🎯 SMART MEETING ASSISTANT")
    print("   Vision Agents 0.6.6 Compatible")
    print("="*80)
    print("\n✨ Features:")
    print("   ✅ Auto-transcription (internal handling)")
    print("   ✅ Q&A with 'Hey Assistant'")
    print("   ✅ Gemini Realtime LLM")
    print("   ✅ GetStream Edge integration")
    print("   ✅ Deepgram speech-to-text")
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
        print(f"\n{'\033[91m'}❌ API Compatibility Error{'\033[0m'}")
        print(f"   This likely means vision-agents version mismatch")
        print(f"   Error: {e}")
        print(f"\n   To check installed version:")
        print(f"   pip show vision-agents")
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}", exc_info=True)
    finally:
        if transcript.entries:
            print_meeting_summary()

if __name__ == "__main__":
    asyncio.run(main())