
GUIDE_MOTHER_LINES = {
    1: "She stood exactly where you're standing and asked the lanterns why they still burn. I liked her question. Better than most people's.",
    2: "She didn't fall into anything down here. People don't fall into rivers this deliberately. She descended completely of her own free will.",
    3: "This hall still remembers a shape she taught it  three children, one table, one argument about who got the last good seat. She's the reason the labyrinth knows what your family sounds like at all.",
    4: "By the time she reached the tombs she had stopped asking whether death could be undone. She'd moved on to asking what it would cost. That's a very different question, and a much more dangerous one to get an honest answer to.",
    5: "At this crossroads, she paid something. I know the shape of a payment being made. I don't know the price. Those are different kinds of knowing, and I only have the one.",
    6: "She stood in front of something enormous down here and refused to be impressed by it. I don't admire much. I admired that.",
    7: "By this floor, she wasn't hunting for a way to bring your father back anymore. She was hunting for a way to apologize to him properly. That's a much harder thing to find than a miracle.",
    8: "The witch offered her a bargain. First she said no. Then, later, she said yes. I don't think she ever decided which of those two answers was the true one.",
    9: "This close to wherever she was going, she stopped writing anything down. I think she already knew how the story ended, and didn't especially want the proof lying around for you to find.",
    10: "Whatever is waiting past this point is not your father wearing a labyrinth. It is a labyrinth that has been wearing your father for a long time, and has started to forget the difference. Ask it the question directly. It owes you that much.",
}

GUIDE_SELF_LINES = [
    "\"What am I? A folded piece of the labyrinth's handwriting that got tired of staying flat. Ask me something with a cleaner edge next time.\"",
    "\"I was a person's name, once, before I was a bird's shape. The labyrinth kept the shape and lost the name. I've made my peace with the trade. Mostly.\"",
    "\"You want to know if I chose this. I want to know if choosing is even the right word for something that happens to you slowly, one fold at a time, until there's no version of you left that remembers being flat paper.\"",
    "\"Here's the whole truth, since you keep asking and I'm apparently the type to eventually give in: I was someone the labyrinth liked enough to keep. That is not the same as being someone it was kind to.\"",
]

RIDDLES = {
    1: [(
        "A lantern near the entrance is carved with words that seem to watch you read them:\n"
        "\"I am lit by no oil and fed by no wick, and the dead insist I have always been burning. What am I?\"",
        ["A memory", "A curse", "An actual lantern, don't overthink it", "A lie"],
        0,
        "The carving warms, just slightly, as though something has been recognised rather than answered.",
        "The lantern gutters, unimpressed. Nothing happens, which is somehow worse than something happening."
    )],
    
    2: [(
        "A tablet half-submerged in the black river reads: \"I have no mouth, yet I swallow names. Cross me once and you are remembered. Cross me twice and you are erased. What am I?\"",
        ["The river", "Grief", "Time", "A door"],
        0,
        "The water goes still for exactly as long as it takes to be sure you're right.",
        "The river keeps moving, entirely unbothered by your guess."
    )],
    
    3: [(
        "Frost has spelled a question into the long table: \"I set a place for guests who never arrive, and I never learn to stop. What am I?\"",
        ["Hope", "A habit", "Grief", "A trap"],
        1,
        "The frost eases back from one plate, as if a seat has finally, quietly, been un-set.",
        "The frost thickens instead, entirely unmoved by your guess."
    )],
    
    4: [(
        "A cracked scale on the tomb wall asks: \"I weigh what a life added up to, and I have never once been wrong, and I have never once been kind about it. What am I?\"",
        ["Judgment", "A scale", "Death", "Truth"],
        0,
        "The scale's needle drifts, briefly, to a resting position that looks almost like relief.",
        "The needle swings wildly and settles nowhere. Some questions just don't like being guessed at."
    )],
    
    5: [(
        "A voice at the crossroads asks from three directions at once: \"Take any of my roads and you'll arrive. Take all of them and you'll never leave. What am I?\"",
        ["A choice", "A crossroads", "A trick", "A test"],
        1,
        "All three directions go quiet at the same moment, which feels, unmistakably, like approval.",
        "The roads keep talking over each other. You didn't fail, exactly. You just didn't finish."
    )],
    
    6: [(
        "Carved beneath a name scratched into illegibility: \"Say me once and I am a title. Say me twice and I am a warning. What am I?\"",
        ["A god's name", "A boast", "A rumor", "A king"],
        0,
        "The colonnade's echo softens, like a room deciding you're not the threat it assumed you were.",
        "The echo repeats your guess back at you, mockingly, and offers nothing further."
    )],
    
    7: [(
        "A star-shaped scar in the stone reads: \"I only come when the light forgets itself, and I am always hungry, and I have never once been full. What am I?\"",
        ["An eclipse", "Hunger", "The dark", "A star"],
        0,
        "The scar dims, briefly, as though something enormous just exhaled.",
        "The scar brightens instead, hungrier than before. That was not the answer it wanted."
    )],
    
    8: [(
        "Something in the hut's walls asks in a grandmother's voice: \"I offer exactly one bargain, and I never explain what it costs until after you've already agreed. What am I?\"",
        ["A witch", "A deal", "A trap", "A gift"],
        1,
        "The hut settles on its legs, apparently satisfied, which is somehow the most alarming sound in the whole floor.",
        "The hut shifts its weight and says nothing further. You are not owed a second guess."
    )],
    
    9: [(
        "Carved into the barrow's threshold in a hand that isn't shaking, exactly: \"I ride without a head and still know exactly whose name to call. What am I?\"",
        ["Death", "A rider", "A herald", "An omen"],
        2,
        "Somewhere in the barrow, something almost sounds like it's laughing, in a way that is not entirely unkind.",
        "Nothing answers. The silence afterward is somehow more pointed than a wrong-answer buzzer would have been."
    )],
    
    10: [(
        "There is no carving here, only a voice that sounds like it's reading from something. \"I am the question your mother never let you ask. What am I?\"",
        ["Why did you leave", "Do you love us", "Are you coming back", "Was it worth it"],
        0,
        "The voice doesn't answer, exactly, but it stops sounding like it's about to leave.",
        "The voice goes quiet in a way that feels less like silence and more like withheld comment."
    )],
}

LORE_FRAGMENTS = {
    1: ["The page is damp, but not with water. \"Grief,\" someone has written, crossed out, and then written again, larger, as though the first attempt hadn't been honest enough about the size of it."],
    
    2: ["A stone tablet, half-eroded: \"She did not fall into the river. She asked it, politely, the way you ask a door to open rather than a wall to move, and it let her through because it had never been asked before.\""],
    
    3: ["Frost has preserved a single sentence on the hall's wall: \"He kept the feast running long after the guests stopped coming, because an empty table is a kind of grief you can pretend is just bad timing.\""],
    
    4: ["A shattered scale lies beside a name filed down to nothing. Someone weighed themselves here, alone, and did not like the number they got, and tried very hard to make sure nobody else would ever see it either."],
    
    5: ["A merchant's abandoned ledger, mid-sentence: \"...paid the toll, though I could not tell you in what currency, only that I have felt lighter every day since, in a way I can no longer entirely call relief.\""],
    
    6: ["A worshipper's forgotten prayer scratched under a defaced name: \"I am not asking you to fix what happened. I am asking you to at least agree that it happened, because everyone else has stopped.\""],
    
    7: ["A star-priest's final entry, mid-ritual: \"We were told the sky forgets nothing. Nobody warned us that not forgetting and forgiving were never the same verb.\""],
    
    8: ["A traveler's note nailed to the hut's fence: \"It offered me exactly what I wanted. I have never been more certain a kindness was a weapon.\""],
    
    9: ["Scratched into the barrow wall by someone who clearly ran out of time to finish: \"The rider doesn't take you because you did something wrong. It takes you because your name finally came up. That's the part nobody—\""],
    
    10: ["There is a single unfinished sentence carved into the shrine's threshold: \"If you have come this far, then I need you to understand that I never meant for—\" It stops there. Whatever came next, someone decided partway through that it didn't need saying, or couldn't be."],
}
