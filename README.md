# k8s-DevOps
Build a DevOps environment on Kubernetes using open source tools.

The goal of this project is to create a devops pipeline that can be used to continually test the instructions contained in digitally available content, such as workshops, tutorials and online course material.

With cloud platforms and modern software development methodologies it is often not possible to specify the versions of software needed to complete an online activity.  The rate of change of underlying platform and services is also an issue which can lead to lots of outdated material, with the authors often not aware that their content is broken.

Checking that content is current is a task many authors do not do, as it can be very time consuming, but outdated content frustrates developers that waste their time following content that they end up having to fix or abandon.

Automating the process of testing instructions contained in online content is the prime goal of this project, so authors can create their content using agile methodologies with a devops pipeline to manage the lifecycle of digital assets.  The DevOps tooking then can automatically test that the instructions contained in each article are still valid and flag up and outdated content.  

The primary difference is that the devops pipeline is not always driven by source control, but by a scheduler, with all projects undergoing continual deployment and testing, so changes in environment or new releases of software which break the instructions in the article are automatically caught during the scheduled deploy and test cycles.
