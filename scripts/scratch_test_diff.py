import sys
sys.path.insert(0, 'backend')
import os
import asyncio
from services.tts_backend import _get_clone_prompt, _clone_prompt_key
from services.model_manager import get_model

async def test():
    model = await get_model()
    voices_dir = os.path.join(os.environ['APPDATA'], 'OmniVoice', 'voices')
    p1 = os.path.join(voices_dir, '2cdaa056.wav')
    t1 = "Here's a quick sample of this voice so you can hear how it sounds."
    p2 = os.path.join(voices_dir, '079904a9.wav')
    t2 = "Na escuta? Aqui é a Dra. Lis. Graças a Deus o seu sinal conectou."
    
    k1 = _clone_prompt_key(p1, t1, True)
    k2 = _clone_prompt_key(p2, t2, True)
    print('k1:', k1)
    print('k2:', k2)
    
    prompt1 = _get_clone_prompt(model, p1, t1, True)
    prompt2 = _get_clone_prompt(model, p2, t2, True)
    print('prompt1:', prompt1)
    print('prompt2:', prompt2)

if __name__ == '__main__':
    asyncio.run(test())
