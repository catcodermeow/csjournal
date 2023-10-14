# Design Document
This file should discuss how you implemented your project and why you made the design decisions you did, both technical and ethical. Your design document as a whole should be at least several paragraphs in length. Whereas your README.md is meant to be a user’s manual, consider your DESIGN.md your opportunity to give the staff a tour of your project underneath its hood.

## Technical Decisions
### In this section, share and justify the technical decisions you made.

You don't need to respond to all questions, but you might find some of the following helpful:

* What design challenge(s) did you run into while completing your project? How did you choose to address them and why?

Some design challenges I ran into while completing my project was creating the "Cheer Me Up" button that generates a random image from a folder of images. I tried a lot of different methods, but the image files would not display on the website and so ultimately using Javascript and hardcoding the image file names into an array to select a random element from worked best. In the future people may want to upload their own images or I might want to add new images to a folder without having to worry about adding all the file names to the Javascript so if I had more time I would figure out a way to simply randomly select a file from a folder. In addition, the random images generated are currently limited by what is uploaded, so in the future I might look into a website that hosts a lot more images that I can use.

I also struggled with adding a pop-up to display the full details of a journal entry. I wanted the user to be able to click a title in the table of journals and then have a window popup on the same webpage displaying the full journal entry. I tried checking out if there was anything documented on Bootstrap that I could use and found a feature called Bootstrap Cards that could potentially work, but I unfortunately wasn't able to explore that enough to implement into my website successfully. Ultimately I just decided to redirect users to another webpage that would display the full journal details. For the full journal details, I used another Bootstrap element called list-group-item that was helpful in containing the journal entry in a nice format.

* Was there a feature in your project you could have implemented in multiple ways? Which way did you choose, and why?

A feature in my project that I could have implemented in multiple ways was the random cat picture aka the "Cheer Me Up" button. I could have used Python to implement the random image selector as well but I couldn't make it work so I just used the hardcoded Javascript.

## Ethical Decisions
### What motivated you to complete this project? What features did you want to create and why?

I was motivated to complete this project because journaling really helps me deal with my stress and feelings. CS is very tough and I wanted to inspire new coders to continue trying and learning so I wanted to create features that would help people deal with and overcome CS roadbumps because there are a lot of learning curves. What personally helps me is having a place to vent about my thoughts and feelings so I created a journals page where users can write and store their journal entries with the intention of each entry documenting their "CS Journey" through a series of journals.

What also helps me is having small goals to work towards to give me direction when learning something new. It was important that these goals are as customizable as possible because everyone works in different ways, so I made sure to include an edit and delete button. Feelings of accomplishment when completing those goals also help fuel my desire to learn more and keep completing goals so I also made to sure to include a checkbox that records when you reach a goal.

I also wanted to have an "Inspiration" page that encourages and inspires people to keep going on their CS Journey. It's easy to get stuck and feel down, so I implemented the "Cheer Me Up" button to generate random cute pictures of my cat because I love her a lot. Other users may prefer something else like a CS meme, so personalizing that feature would be a fun addition. In addition, I attended the AI Bot Building Hackathon by Steamship and we were able to make a bot that has a personality. I decided to create a bot with an encouraging personality that always refers to the user as "clever coder" and adds a motivational quote. Sometimes it is nice to have someone to vent to about how you're feeling and have them just unconditionally listen and support you, so I thought a friendly bot that is cheering you on would be a good addition.

Finally, I decided on a minimalistic color scheme of blue and grey because they give off calm vibes.

### Who are the intended users of your project? What do they want, need, or value?
You should consider your project's users to be those who interact _directly_ with your project, as well as those who might interact with it _indirectly_, through others' use of your project.

Intended users of my project who may interact directly with my project are new CS students, people trying to pick up a new skill and people who enjoy journaling or writing out their thoughts. They want an encouraging space to document their journey in learning CS and celebrate their progress however big or small.

People who might interact with it indirectly are parents, friends, coworkers of the direct users.

### How does your project's impact on users change as the project scales up?

* How could one of your project's features be misused?

As AI is still not completely reliable, it is possible for people to perhaps prompt the AI Bot in a specific way that makes it respond in a negative or offensive way.

Depending on what the user is venting about, the journal contents themselves could also be bad.

* If your project becomes widely adopted, are there social concerns you might anticipate?

If my project becomes widely adopted, there are some social concerns like the security of people's data and privacy. If the site becomes more popular, hackers could try to steal data so I would need to work on securely storing it.
