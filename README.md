Filter Torre

This project use the api of torre.co with this endpoints:

GET https://torre.bio/api/bios/$username (gets bio information of $username)
GET https://torre.bio/api/people/$username/connections?[q=$query&limit=$limit] (lists people sorted by connection degrees relative to $username)


What its does?

Given these endpoints, an flask aplication was builded to retrieve this endpoints
With the first route, information about the user and his contacts was obtained (name, professional head line, summary of biography, education, strengths, language and location)

with the second route information about the user's contacts was obtained

How to use

You can visit the app with this link: xica.tech/api/v1/ + endpoint

Endpoints

There are 8 endpoints and it is always necessary to start with the validate to start the CONNETIONS list:
1. /status -> return the status of the api

2. /validate/$publicId -> initialize the CONNECTIONS list and return a list with the contacts, their name and publicId
3. /language/$language -> returns a list of the user's contacts that have the specified language. Update the CONNECTS list. If a filter has been previously applied, the search will be done using the previously filtered contacts.

4. /education/$education -> returns a list of the user's contacts that have the specified education. Update the CONNECTS list. If a filter has been previously applied, the search will be done using the previously filtered contacts.

5. /strengths/$strengths -> returns a list of the user's contacts that have the specified strength. Update the CONNECTS list. If a filter has been previously applied, the search will be done using the previously filtered contacts.

6. /location/$location -> returns a list of the user's contacts that have the specified location. Update the CONNECTS list. If a filter has been previously applied, the search will be done using the previously filtered contacts.

7. /person/$publicId -> returns a list with name, profesional head line, summary of biography, education, strengths, languages and the location of the person

8. /clear -> clean the CONNECTIONS list


Or clone this repository and run in local:

You have to get installed python 3.4 at least:

$ sudo apt-get update
$ sudo apt-get install python3.4

Run this command to install the requirements:

$ pip3 install -r requirements.txt

Then, you can run locally as developing enviroment with:

API_PORT=5000 API_HOST=0.0.0.0 python3 -m api.v1.app

In the browser you can consume the API with the following route:
http://localhost:5000/api/v1/ + endpoint as explained above
