# neuroflow-challenge
challenge assignment for neuroflow

# Setup

Install docker. Then run
```
docker-compose up --build --remove-orphans
```
The backend will be running on localhost:5010 and the frontend on localhost:5000. However, the frontend does take a while to setup since it's running npm start.

If you want to run frontend separately, look at the Running frontend separately section below.

If running into issues, please check the Known issues at the very bottom!

# How to use

Once the app is up and running, 
1. Go to localhost:5000 in a browser
2. Click register and enter your email, first name, last name, and password. This will save your data(after hashing the password) in a user table and return a token.
3. Now, you should see a screen with a text box and a button. If you enter a value between 0 and 10 and press submit, you should see a new mood pop up. This is getting sent to the server along with the token to add a mood associated to the user.
4. On a new day, if you still have the program running(reseting the backend resets the db), you can press submit and see the streak becomes 2. The calculation method used for the streak is listed below.
5. To login without creating an account, reload the page to get back to the login page and press login and enter your email and password.

# Scalability and improvements
This is the answer to the question

Document what, if anything, you would do differently if this were a production application and
not an assessment? What tech would you use? How would you handle things differently if it
needed to handle more users, more data, etc?

Here are the list of things I'll do differently
- The authentification method currently of having a token in the header and checking it for every single request, while great for security, is not scalable. This is because doing a db check that much unnecessarily is a cause of slow performance especially with a lot of users. Replacing this with redis and caching might be better.
- If there's issues of too much data for one db, I recommend partitioning the mood table across databases depending on the date of creation for mood. This can be achieved by putting an upper limit on the streak(100 days) and moving the records before 100 days ago to another database. If those 100 days of data is still too much, we can subdivide into n number of databases where each database is responsible for 100/n days of mood values.
- The creating user takes a while due to bcrypt being slow. This is a trade off of security vs convenience but I think lowering the length of the salt I added to the password when saving for security can be lowered.
- The docker image for the frontend is slow as I'm doing npm start and it's running in debug mode. A better approach is run npm run build and convert to html then host on a node server.
- The flask app is running in debug mode which is bad for performance in production.
- In production mode, which can be set via env variable, the flask app will run using wsgi. A further nginx layer will be even better.
- For easy scalability, using kubernetes deployment for each of these services might do well. Since they are all dockerized, it shouldn't be too hard.
That is all off the top of my head.
# Running frontend separately
1. Comment out the frontend portion of the docker-compose.yaml by turning
```
  frontend:
    build: ./frontend
    volumes:
      - ./frontend:/app
    ports:
      - 5000:5000
    depends_on:
      - backend
    environment:
      - REACT_APP_API_URL=http://localhost:5010
      - PORT=5000
    restart: unless-stopped
```
into
```
  # frontend:
  #   build: ./frontend
  #   volumes:
  #     - ./frontend:/app
  #   ports:
  #     - 5000:5000
  #   depends_on:
  #     - backend
  #   environment:
  #     - REACT_APP_API_URL=http://localhost:5010
  #     - PORT=5000
  #   restart: unless-stopped
```
2. Create a .env file with the contents in the frontend/ directory
REACT_APP_API_URL="http://localhost:5010"
PORT=5000
3. Install yarn and npm
4. Still in the frontend/ directory, do
```
yarn
npm start
```
and the frontend should be up in a while!

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
- [x] Create an user table in the database
- [x] Create a token table for a token for each user
- [x] Add user relationship with the mood table
- [x] Create a create user endpoint given username and password
- [x] Create a login endpoint given username and password and generates a token
- [x] To the /mood endpoint, add a token parameter in the header
- [x] Create a react app
- [x] Create api.js for posting to mood, creating user, and logging in
- [x] Create basic redux setup to store information
- [x] Create ui for login/signup
- [x] Create ui for posting mood
3. Create a '/mood' endpoint with a GET method, returning all values submitted by the logged-in
user.
- [x] Create get mood endpoint
- [x] Add to api.js
- [x] Add to redux
- [x] Add to ui
4. Add to the body of the response for the ‘/mood’ endpoint the length of their current "streak".

A user is on a “streak” if that user has submitted at least 1 mood rating for each
consecutive day of that streak.

For example, if on March 1st, March 2nd, March 3rd, and March 5th the user entered
mood ratings, a 3-day streak will apply to the March 3rd rating and the streak will reset to
a 1-day streak for the March 5th rating.

- [x] To the mood table add a streak column
- [x] When mood is posted, and streak is 0, set streak to 1. Otherwise, if there was a mood one day ago, add 1 to the streak and save it.
- [x] Have ui

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