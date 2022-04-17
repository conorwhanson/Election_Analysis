# Colorado Congressional Election Audit & Analysis
The purpose of this project was to audit and analyze voting data in a local Colorado congressional election. 

## Resources
- Data source: election_results.csv
- Software used: Python 3.9.7; Visual Studio Code 1.66.0

## Results
- The total votes cast in this election was 369,711.
- Arapahoe county cast 24,801 votes, or 6.7% of the total vote; 
    Jefferson county cast 38,855 votes, or 10.5% of the total vote;
    Denver county cast 306,055 votes, or 82.8% of the total vote. 
- The county votes distribution was heavily biased to Denver county, which received 83% (306,055) of the total number of votes cast in the election.

    ![County_votes_summary](https://github.com/conorwhanson/Election_Analysis/blob/main/resources/county_summary.png)

- Candidates on the ticket and their results: Raymon Doane received 11,606 (3.1% of the total) votes; Charles Stockham received 85,213 (23% of total) votes; Diana DeGette received 272,892 (73.8% of the total) votes.
- Diana DeGette won this election in quite a landslide victory, receiving the vast majority of votes: 272,892 which made up 73.8% of total votes cast. See image below for winner calculation.

    ![winning_candidate](https://github.com/conorwhanson/Election_Analysis/blob/main/resources/winning_candidate.png)

## Summary of Election-Audit
How this script can be used for any election in the future, with at least two examples of how the code can be refactored for future purposes.

This script worked well for the analysis goals of this particular election. It could certainly be used for future elections, albeit with a few modifications depending upon what the analysis goal(s) would be. Two examples will suffice to show this. First, it may be useful to track the candidate votes based on county. In the below portion of the code, where the candidate names and counties were pulled from the dataset, we could easily insert a conditional (after line 78) to count candidate votes based on county and save that to a set of variables (defined before the script runs). 

![candidate_county_data](https://github.com/conorwhanson/Election_Analysis/blob/main/resources/candidate_county_data.png)

This could be very useful to analyze the popularity of each candidate based on the county, particularly as it relates to the candidate's respective platform and that platform's popularity in each county. This would help fill out a picture of the demographics and socio-political tendencies of each county.

Second, the script could be used in conjunction with county population data to see the turnout of each county as it relates to that county's total population (voting age, of course; or perhaps registered voters). Another csv file could be read in, which would contain population and voter registration data for each county. A simple calculation could then be placed within the for-loop beginning on line 112 (after the county turnout of total votes was calculated) in the image below.

![county_turnout](https://github.com/conorwhanson/Election_Analysis/blob/main/resources/county_turnout.png)

This would be potentially helpful to which counties are most politically engaged based on their total pool of registered voters/population. Further, if a particular county has a trend of high voter turnout, this could be discovered and perhaps anticipated in future election analyses and audits. This could help fill out a picture of the overall expected political activity of each county, especially as it relates to that county's socio-political tendencies noted above.