# Crowdfunding Back End

Bianca Di Biase

## Planning:

### Concept/Name

Books for Change is a service that distributes real, physical books to metro and regional communities across Australia. We also offer educational programs to help improve literacy as well as reading and comprehension skills for all ages. Books can give ideas, open minds, expand perspectives, offer growth and learning, and show people what’s possible. We believe that the gift of reading is something that can and should be available to everyone.

_ Books for love _ Books for growth _ Books for hope _ Books for justice _ Books for power _ Books for learning _ Books for possibility _ Books for healing _ Books for connection _ Books for understanding _ Books for diversity _ Books for inclusivity

### Intended Audience/User Stories

The target audience for Books for Change are individuals, groups and companies who are interested in helping empower and uplift others through book distribution and education, particularly those in marginalised communities.

### Front End Pages/Functionality

- {{ A page on the front end }}
  - {{ A list of dot-points showing functionality is available on this page }}
  - {{ etc }}
  - {{ etc }}
- {{ A second page available on the front end }}
  - {{ Another list of dot-points showing functionality }}
  - {{ etc }}

### API Spec

{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page.

It might look messy here in the PDF, but once it's rendered it looks very neat!

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL | HTTP Method | Purpose | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ------- | ------- | ------------ | --------------------- | ---------------------------- |
|     |             |         |         |              |                       |                              |

### DB Schema

![]( {{ ./relative/path/to/your/schema/image.png }} )

### A link to the deployed project.

### A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.

(./images/screenshotget.png)

### A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.

(./images/screenshotpost.png)

## A screenshot of Insomnia, demonstrating a token being returned.

(./images/screenshottoken.png)

## Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).

Step One: To create a new user in Insomnia, start by creating a new HTTP Request, changing Get to Post, click on Body, change text to JSON and enter username, password and email. The http address next to post should end in /users/.
(./images/screenshotstepone.png)

Step Two: Next, replace /users/ with /api-token-auth/ in the post http address. Log in user details to generate a token.
(./images/screenshotsteptwo.png)

Step Three: Next, click on Auth, choose Bearer Token from the dropdown list, copy the token generated in the previous step, and paste in the Token field. Write the word token in the Prefix field.
(./images/screenshotstepthree.png)

Step Four: Make sure /projects/ is at the end of the Post http address. In the body field (JSON), fill in the following fields: title, description, goal, image, is_open and owner.
(./images/screenshotstepfour.png)

## Project Requirements

Your crowdfunding project must:

- [ ] Be separated into two distinct projects: an API built using the Django Rest Framework and a website built using React.
- [ ] Have a cool name, bonus points if it includes a pun and/or missing vowels. See https://namelix.com/ for inspiration. <sup><sup>(Bonus Points are meaningless)</sup></sup>
- [ ] Have a clear target audience.
- [ ] Have user accounts. A user should have at least the following attributes:
  - [ ] Username
  - [ ] Email address
  - [ ] Password
- [ ] Ability to create a “project” to be crowdfunded which will include at least the following attributes:
  - [ ] Title
  - [ ] Owner (a user)
  - [ ] Description
  - [ ] Image
  - [ ] Target amount to fundraise
  - [ ] Whether it is currently open to accepting new supporters or not
  - [ ] When the project was created
- [ ] Ability to “pledge” to a project. A pledge should include at least the following attributes:
  - [ ] An amount
  - [ ] The project the pledge is for
  - [ ] The supporter/user (i.e. who created the pledge)
  - [ ] Whether the pledge is anonymous or not
  - [ ] A comment to go along with the pledge
- [ ] Implement suitable update/delete functionality, e.g. should a project owner be allowed to update a project description?
- [ ] Implement suitable permissions, e.g. who is allowed to delete a pledge?
- [ ] Return the relevant status codes for both successful and unsuccessful requests to the API.
- [ ] Handle failed requests gracefully (e.g. you should have a custom 404 page rather than the default error page).
- [ ] Use Token Authentication, including an endpoint to obtain a token along with the current user's details.
- [ ] Implement responsive design.

## Additional Notes

No additional libraries or frameworks, other than what we use in class, are allowed unless approved by the Lead Mentor.

Note that while this is a crowdfunding website, actual money transactions are out of scope for this project.

## Submission

To submit, fill out [this Google form](https://forms.gle/34ymxgPhdT8YXDgF6), including a link to your Github repo. Your lead mentor will respond with any feedback they can offer, and you can approach the mentoring team if you would like help to make improvements based on this feedback!

Please include the following in your readme doc:

- [ ] A link to the deployed project.
- [ ] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a token being returned.
- [ ] Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
- [ ] Your refined API specification and Database Schema.
