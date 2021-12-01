# neuroflow-challenge
challenge assignment for neuroflow

# Setup

Install docker. Then run
```
docker-compose up --build --remove-orphans
```
The backend will be running on localhost:5010

Save requirements from conda env:
```
pip list --format=freeze > requirements.txt
```
# Requirements
1. Create a web REST application with a '/mood' endpoint, which when POSTed to persists the
submitted mood value.
- [x] Create conda env
- [x] Create a flask app
- [x] Create a table in the database for mood
- [x] Create a post request endpoint for '/mood' which gets a value.
- [x] When mood value is sent to the endpoint, save it to the database
- [x] Create requirements.txt
- [x] Make dockerfile
- [x] Setup docker-compose.yaml with database

2. Add the ability for users to login.
- [ ] Create an user table in the database
- [ ] Create a token table for a token for each user
- [ ] Add user relationship with the mood table
- [ ] Create a create user endpoint given username and password
- [ ] Create a login endpoint given username and password and generates a token
- [ ] To the /mood endpoint, add a token parameter in the header
- [ ] Create a react app
- [ ] Create api.js for posting to mood, creating user, and logging in
- [ ] Create basic redux setup to store information
- [ ] Create ui for login/signup
- [ ] Create ui for posting mood
3. Create a '/mood' endpoint with a GET method, returning all values submitted by the logged-in
user.
- [ ] Create get mood endpoint
- [ ] Add to api.js
- [ ] Add to redux
- [ ] Add to ui
4. Add to the body of the response for the ‘/mood’ endpoint the length of their current "streak".

A user is on a “streak” if that user has submitted at least 1 mood rating for each
consecutive day of that streak.

For example, if on March 1st, March 2nd, March 3rd, and March 5th the user entered
mood ratings, a 3-day streak will apply to the March 3rd rating and the streak will reset to
a 1-day streak for the March 5th rating.

- [ ] To the mood table add a streak column
- [ ] When mood is posted, and streak is 0, set streak to 1. Otherwise, if there was a mood one day ago, add 1 to the streak and save it.
- [ ] Modify the get endpoint if necessary

# Known issues
1. 

Problem:

Some applications can't connect to the db with error: no pg_hba.conf entry for host

Resolution:

You may need into the data/pg_hda.conf and add the line 
```
host    all  	        all  	        0.0.0.0/0           trust
```
for all applications to access the db. NEVER do this in production