# Digital Asset Creation Best Practice

**TODO**
Currently this is just a brain dump - needs reorganising and writing up

## Before creating any content

- Are the objectives of the proposed content well understood?
  - who is target audience
  - what is the 'level' of the article beginner, advanced?   [Blooms Taxonomy](https://en.wikipedia.org/wiki/Bloom%27s_taxonomy) can help here
- What type of content is appropriate?  Blog post, step-by-step instructions, multi-part workshop, full blown online course?
- How will you present the content?  Written, video, audio or combination of content types?  Sometimes a video or image can add clarity in a complex environment

## Creating content

- Ensure all prerequisites are specified up front, especially any which may incur costs or require a credit card for authorisation/account setup
- If a particular instruction is not obvious or can't be well understood (when all the prerequisites are met) then additional context and links to additional resources should be provided.
- Be aware of assumed knowledge.  It is very easy to assume the developers following your content understand acronyms you use every day, are familiar with the tools and user interfaces you use every day - unless you have explicitly called out the assumed knowledge as a prerequisite.
- Be clear when using terms like console.  In many cloud environments every service has a console in addition to the main cloud console, so ensure your content makes it clear which console you are referring to.
- Use links to make the developers consumption of your content easier.  If you say "install the command line tools", make **"Command line tools"** a link to instructions on where to download and install the tools.
- If there is an authoritative source of information on a topic, don't repeat the material, link to the authoritative source (e.g. IBM Cloud documentation)
- Are you using developer best practices in your content.  Your sample code should be inline with accepted best practices.
  - E.g. if creating a cloud application then 12-factor app best practices should be applied.
- Keep your content realistic.  If you say you are creating a production ready example for a developer to extend and build upon, then ensure it is production ready:
  - Are the the require testing artifacts included (production ready content should include test artifacts?)
  - If you say production ready, but the code has no error handling then it is not production ready
  - Production ready code should take security requirements into account - using unencrypted communication over public internet or unsecured API endpoints is not production ready
  - Add comments if you are deliberately removing production ready requirements to facilitate presenting more understandable code focussing on the target area of the content
  - Ensure you have some date present so a developer can quickly tell if the content is likely to be up to date or out of date.  If git based then git provides dating evidence but many blog sites do not.  Keep date information up to date when manually specified and you update content
  - Call out when you are requesting a developer to install the latest available version of something or are using a specific version.  If you are installing latest version, provide some indication of what version you actually installed, as version mismatch can be where issues arise

### DevOps automation of content

- When automating, ensure scripts reflect article instructions.  Don't tell developer to run a command, then achieve the same result by creating an application.  Your scripts should be running the commands you tell developers to use
- When manual steps can't be automated, ensure that any workaround produces the same results (e.g. re-flashing a raspberry pi back to fresh install state.)
- Ensure config is not embedded in scripts.  If a developer wants to extend/use your content and deploy their own automation, then they should simply be able to change config and the automation should still work.
- Enable developers to quickly find out all version information used in latest successful test.
- Have a consistent CI/CD build environment, remove any potential differences such as host OS differences.  It is usually possible to specify the environment, such as a Docker container, where all build and deploy activity takes place.

## Review content

- does the created content match the objectives set out?
  - A list of instructions does not usually deliver learning or understanding.  It just mean a developer mean a developer is able to follow a list of commands - Ideally we should be aiming for a developer to be able to apply the subject of a digital asset to their own project(s) rather than just replicating a sample.
  - Is the level correct - to trivial or too advanced?
- Review the content from the view of someone new to the tools/platforms/technology you are using - unless you have explicitly called out the knowledge in the prerequisites.  Will a developer be able to get through the content, or will they encounter 'break points', where they need to do additional research to be able to continue to follow the content?
- Test every instructions and ask yourself:
  - Does the instruction make sense without applying assumed knowledge?
  - Is it clear where the instructions needs to be carried out (which console, on which machine, .....)
  - Will the developer understand what the instruction does and why they need to do the requested action - if not do you provide any links to allow a developer to gain an understand of key concepts?