# Vibe Coding an Electronic Music Ticket Platform Fake Data Generator

I've been ruminating for quite some time about working on a personal project that can help me hone the skills I need for my job as a Data Consultant. I've always found "data problems" to be a bit harder to reduce down into a personal project - mostly due to most problems mostly happening at enterprise-level (e.g. scalability issues, data quality, legacy systems...).

Therefore, I wanted to create a fake dataset? (not sure if that is the right word) to approximately recreate that data landscape so that I can use it throughout different challenges & learn data skills in practice. 

Being the club rat that I am (I guess I should say _was_ - I'm almost 26 and my knees can't take it), I finally decided on mocking a ticketing platform, focused on electronic music events. 

I'll be using this dev diary as a lab book, so that I can track my progress & discuss challenges that I will find as I work on synthetix.

## 4th of July

I was finding it a bit hard to kick-start this project and I eventually reached a breaking point and downloaded cursor, with the aim of letting go of some of my apprehension of using AI for learning.
Unsurprisingly, it went very well, it quickly got me to a point where I could generate data, in a very well-organised repo even with my rusty python skills.

However, no matter the _vibe codingness_ , I was not satisfied with the data architecture itself, and no matter the number of prompts, it was slowing becoming more clear that I had to do something unimaginable: stop and think.

> side note: i am so dramatic, why did I chose to do a lab book when every time I write I just slowly descend into ??? I don't even know how to describe this. ANYWAYS.

I had issues defining roles in the app (e.g. who creates the events? who should have access to edit the event?), I could not figure out a technical solution on how are tickets validated on the night and I could not describe the relationship between ticket/purchase/owner in a way that made sense to me.

At this point, it was clear I had to bring pen to paper and sketch out the system in depth.

Also, my main aim with this project was to create a fun dataset that I would be excited to use, and even if I was so impressed by Faker, the content itself was meaningless and in turn - boring. As an example:

| Real Name    | Artist Name | Bio |
| -------- | ------- | ------- |
| Samantha Hickman  | Katrina Smith   | Action own leader theory rise weight much.  |

Therefore, I think I'll be using some degree of scraped data (or maybe even using an LLM) to generate more realistic sounding values.

Finally, for the data challenges I'll be working through with this data, I need it to have data quality issues, to be complex, & ideally show a degree of realness for analytics exercises down the line (e.g. London having more events). I'm not yet very sure on how I can make this happen.

Overall, I'm quite happy with my vibe coding start - it got me started - which as you will know, it's always the trickiest bit.


## 13th of July
Can I vibe code architecture/data modelling exercises? Yes, mermaid JS