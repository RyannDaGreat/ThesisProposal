# Transcript of user requests

Near-verbatim, courtroom style. The user dictates by voice-to-text; clear speech-to-text errors are fixed and marked [sic → fix] where the meaning was a guess.

## 2026-11-22 18:20 (session "ThesisPoint")

> So what you can see here is that I have a thesis that I've written and I have a bunch of random slides and a bunch of PowerPoint presentations that eventually I need to make my presentation for tomorrow with. You can use and stay in work mode and analyze all these different presentations, read my thesis, understand everything that there is to understand. And we're gonna have you propose a presentation for me. We're gonna keep it condensed at first, 50 slides, it has to have a good story to it. You gotta balance a few different things.
>
> I'm gonna copy, "Oh my god, stop pestering [sic: "hestering"] me with blah blah blah, would you like to access blah blah blah?" You can take control of my mouse and stuff if you notice there's a problem, like something's taking too long, probably because of a permission [sic: "mission"] error, you can open Python, input stuff, like the control library to control my mouse and take screenshots. Don't do that unless you have to though, it's more efficient to do things headlessly.
>
> Anyway, I just added a bunch of scrawled notes. I'm just gonna put them there, honestly. Might help you. Might not help you, I don't know. It's gonna be called ScrapNotes.txt.
>
> Make sure to keep the GitHub repository clean as you go. And use Sonnet agents for your, well, yeah, I mean, I know that we said this is a fork mode, but really you can use any subagents you want. So... Alright, so you can launch your swarm of Sonnet agents to understand everything there is to know about my thesis and these folders and stuff, while you take a look to understand everything that you need to know.
>
> And we're going to write PowerPoint presentations. We're gonna work on our magnum opus here, which is under presentation. We're gonna have, inside here, I'm gonna make an agent folder where you can do your agent stuff. You can treat that as a dump. And then... There's a file called AIPresentation.pptx. And these are the two things you're allowed to touch now. You can do whatever you want inside the agent folder, but the AI presentation is the only one that will actually look at it. You get it?
>
> Alright. So yeah, it needs to flow nicely. There needs to be a nice story to it. My thesis tells all. My thesis is basically a bunch of my papers duct-taped [sic: "duct-hate"] together sandwiched between the parts that they actually care about, which is the overall outline and stuff like that.
>
> Please, create a draft and try to conform to my, well, conform to, but inherit my styles. I have a very particular way of doing presentations. I don't like boring or especially AI-created looks. I have my own writing style. I don't sound like an AI. I don't do "not this, not that".
>
> Make sure that inside your agents file you transcribe what I ask for and have a manifest and concerns. And right now the state is quite messy and I can't push this. We gitignore all the [sic: "We get ignore alert files" — unclear; read as: the big .pptx files are git-ignored] files, but all other files you can push as you go. Sorry, don't push as you go, but you can commit as you go.
>
> You have 10 minutes to overview everything and then give me a coherent... Well, you can split it up. You can have your agents take five minutes and then give me a coherent presentation proposal.

> Notify me when you're done and talk out loud again. Keep your deadlines in mind, this will be a timed thing. Here's the rules for this session: you can use as many agents as you want, Sonnet agents primarily, to get your job done within a deadline. I'll be giving you deadlines so that I can review you periodically. When I give deadlines you should plan ahead, you should make plans for what you'll get done. When I give you limited numbers of notifications and talking points, you can talk out loud and notify me only when I ask you to. I'm going to give you one notification right now and one talking point right now. I'll tell you how to talk out loud, but don't do it until it's ready because you only have one chance to talk.
>
> Reply in chat first as you would normally. Then speak in pure English via (curl -s -d 'YOUR_MESSAGE_HERE' ntfy.sh/stark_comma > /dev/null &), only 1-2 sentences unless asked for more as it will be played as audio. Note: this will be read out loud to a human, so keep it from being too verbose. Please note: "notify me" refers to "rp call ntfy_send [message]" and "talk to me" refers to speaking with the above curl command (they're not the same).

> Your Sonnet [sic: "jsonnet"] agents can be medium or high effort depending on whatever you want, and if there is something truly difficult, feel free to use Opus agents. That's always on the table.

> /Users/rburgert/Documents/ThesisProposal/presentation

## After draft v1 (2026-11-22 18:41)
> Yeah, this looks like generic garbage. This looks so lazy. This looks beyond lazy. I can't present this. You just took random figures and slapped them on with no understanding of what any of them were or how I would present them. None of it makes any sense. This is terrible. Most slides are just a single picture with like nothing more going on. It doesn't enhance any understanding of these papers or how they connect or what anything about them. You're not even explaining the papers. Like, I can't even explain a single one of these papers or how it works and what you put in there. And when you copy random LaTeX and bullshit into it, it does not help.

## The test (2026-11-22 18:43)
> If you launched an agentic user study, I guarantee none of your agents who read this presentation for the first time would have any clue what the hell I'm talking about. Now what you could have is a potential transcript where you simulate what I'm saying out loud, which again, has to be assuming that I have one hour to present, talking at a normal human voice word rate, the things that I could say to bring them to understand. One of these thesis committee members has never read any of my papers before. This is going to be their first time seeing these things. They understand about what AI is, and that's about a- they understand generative AI, that's a-
>
> That, by the way, should be your test.
>
> You now have one hour to iterate and make it better. You can use a genetic frenzy if you have to. Do whatever you want, but it has to pass agentic user studies that assume, you know what, not even one hour. We're gonna give it that I'm gonna give a 30 minute talk. I'm gonna go through my different papers and they have to understand them. Everything in here has to be understood, given what I say on a given slide and then what they're actually looking at.

## Thesis committee simulator (2026-11-22 18:45)
> Another thing that you should check is not only should the other agents understand it, but for every paper, one little agent who's read the paper, if there's important details that are left out, these will be the thesis committee simulator. If there's any weak points that I missed out that make it less strong, the thesis committee simulator would say, "Heh heh, fuck you, your paper's bad. Ha ha ha." So it's a defense. You should be doing it as a thesis defense. There should be enough inside the slides to explain answers to obvious questions that would be asked. So it's an understanding of the papers. Like, if you come up with a quiz for what these agents should know after this, like the main ideas of the paper and how they're implemented, to, mind you, Dimitris Samaras, Michael Ryoo, and Yifan Sun, these are the three professors that will be on there. You can get an idea of their profile and how they'll be asking very intelligent things, and not just the basics. They can understand things quickly. They'll see through bullshit. What you gave before was a pile of steaming horse crap. Clearly, whoever made that presentation didn't understand what they're making or why.
