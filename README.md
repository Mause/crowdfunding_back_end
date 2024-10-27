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

## Submission

Please include the following in your readme doc:

A link to the deployed project.
A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
A screenshot of Insomnia, demonstrating a token being returned.
Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
Your refined API specification and Database Schema.
