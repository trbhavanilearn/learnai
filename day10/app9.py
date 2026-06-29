text=f'''Football is one of the most popular sports in the world. It is played between two teams of 11 players, and the objective is to score goals by kicking the ball into the opponent's net. A standard match lasts for 90 minutes. Football promotes teamwork, discipline, fitness, and sportsmanship, making it a favorite game for people of all ages.'''

import asyncio
import edge_tts

TEXT=f''' Vanakkam nanbargale. Naan Prabhu. Inniku namma Python programming oda basics pathi kathukaporom. Variables, loops, functions matrum lists epadi use panna vendum nu practical examples oda paakaporom. Daily konjam konjam practice pannina neengalum nalla programmer aaga mudiyum.'''

async def main():
    communicate = edge_tts.Communicate(
        TEXT,
        voice="ta-IN-PallaviNeural"
        #voice="en-US-AriaNeural"
    )
    await communicate.save("output.mp3")

asyncio.run(main())