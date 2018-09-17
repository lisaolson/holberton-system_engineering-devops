# Postmortem

## Issue Summary
2018/9/12 - 2018/9/15 (70 hours)
From September 12th, 3:57am through September 15th, 1:00am, we experienced a site-wide outage spanning just under 3 days causing over 4,000 error messages.  We saw spikes in our monitoring tools reporting 100% of traffic was affected.  Due to the severity of the outage, no users were able to access the site for the entire 35 hours.  The root cause of the outage was unanticipated flooding that ravaged the city.

## Timeline (PT)
- 09/12 3:57am: First error messages begin to show up
- 09/12 5:00am: Dev Ops Engineering lead begins to debug the error messages coming through the monitoring tools. 
- 09/12 6:00am: Outage officially begins, shutting down the site
- 09/12 6:57am: Arrival at the scene to find servers completely flooded, with water still pouring in from the sides and top
- 09/12 7:00am: Dev Ops Engineers begin to check status of backup servers
- 09/12 9:00am: Engineers find data in backup servers to be outdated
- 09/12 5:13pm: Backup server data is corrupted and the re-directed traffic is beginning to shut down the backup servers
- 09/12 11:35pm: Attempts to configure rollback and backup servers
- 09/13 7:00am: Rollback is still completing, we direct our attention to the flooded building itself
- 09/13 12:20pm: Board room meeting with fire department and local volunteers affected by flooding
- 09/13 5:45pm: Decision is made for the safety of team to begin gathering all equipiment and material out of the building
- 09/13 11:59pm: Successfully moves all remaining equipment out of the building and safely exits the scene leaving the rest of the work to the fire department
- 09/14 5:00am: Rain and flooding begins to subside
- 09/14 12:40pm: Rain begins to drain out of the building and running into local water drainage
- 09/14 1:00pm: Backup servers are reconfigured and able to get the site back up and running with redirected traffic
- 09/14 2:00pm: Servers located in other buildings are overloaded by the redirection of traffic now that the site is back up
- 09/14 3:53pm: Site is up and down periodically as the servers are flooded with traffic
- 09/14 4:15pm: Decision is made to shut down site until backup servers are stable
- 09/13 5:56pm: Configuration change rollback is successful
- 09/15 12:00am: Servers stabilize
- 09/15 12:20am: Server restart begins
- 09/15 3:57am: 100% of traffic back online

## Root Cause and Resolution
At 3:00pm PT, torrential downpour began.  Though the buliding containing our primary servers should've been protected, the rain reached a level unprecedented in our city.  It reached the same level as the doors which caused the entire basement containing all our servers to flood after over 12 hours of downpour.  We began to resolve the issue by moving all remaining equipment possible out of the building and trying to get our backup servers online.  We discovered shortly after that the backup servers were overlogged and getting swamped with traffic as we hadn't backed them up recently.  The Dev Ops Engineers worked tirelessly to get the backup servers back up and running while the rest of the team moved all remaining equipment out of the building.  We successfully moved the equipment out and were able to get the backup servers running after 2 and a half days of effort.

## Corrective and Prevantive measures
In the future, we will move our servers above ground, not in the basement.  We will also more periodically back up our extra servers to ensure that they can handle the traffic spikes and also that they are as up to date as our primary servers.  We'll also add monitoring tools to every aspect of our additional servers in case this was ever to happen. Additionally, it would help to have servers located in more than 2 buildings, just in case something of this nature was to happen again.  Ideally, in a more dry state. Aditionally, we will add monitoring tools checking traffic spikes and memory logs to ensure we're gathering all the data we need to meticulously track our backup servers' status.

#### Author
Lisa Olson
