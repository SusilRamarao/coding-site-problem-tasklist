
import leetcode

# Experimental: Or CSRF token can be obtained automatically
import leetcode.auth

class leetclass:

    def get_data():
        
        # Get the next two values from your browser cookies
        leetcode_session = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMjk1NDYzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2JiMmFkNTc4YzNmNGUxNGM1MDEyNTVmZTQzOWI1ODY2YWEzMTU5MiIsImlkIjoyOTU0NjMsImVtYWlsIjoic3VzaWw5NUBnbWFpbC5jb20iLCJ1c2VybmFtZSI6InN1c2lsOTUiLCJ1c2VyX3NsdWciOiJzdXNpbDk1IiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL3N1c2lsOTUvYXZhdGFyXzE1OTg3NjMwMzAucG5nIiwicmVmcmVzaGVkX2F0IjoxNjU3NTQ2ODA3LCJpcCI6IjI0MDI6ZTI4MDoyMTIzOjEwMjo0MTdiOmFiMTc6NWM3YTpiZGIwIiwiaWRlbnRpdHkiOiI3ZTJlNDc1Mjk0N2I1MjIwYzYyM2JkZGMyYmZiN2YxMCIsInNlc3Npb25faWQiOjI0MzEzNDIzLCJfc2Vzc2lvbl9leHBpcnkiOjEyMDk2MDB9.L9LudidFbc9IkLVKnkHUKDtVqb_0WRtnjCupyF_U8n0"

        csrf_token = "ZczpGJfq0sHXxFNbHKLOku7OBSvSYuuky6XpKvC3Q7MVkOTm12u2JmZBZaIK99gH"

        csrf_token = leetcode.auth.get_csrf_cookie(leetcode_session)

        configuration = leetcode.Configuration()

        configuration.api_key["x-csrftoken"] = csrf_token
        configuration.api_key["csrftoken"] = csrf_token
        configuration.api_key["LEETCODE_SESSION"] = leetcode_session
        configuration.api_key["Referer"] = "https://leetcode.com"
        configuration.debug = False

        api_instance = leetcode.DefaultApi(leetcode.ApiClient(configuration))


        graphql_request = leetcode.GraphqlQuery(
            query="""
              {
                user {
                  username
                  isCurrentUserPremium
                }
              }
            """,
            variables=leetcode.GraphqlQueryVariables(),
        )

        print(api_instance.graphql_post(body=graphql_request))


        api_response = api_instance.api_problems_topic_get(topic="algorithms")

        slug_to_solved_status = {
            pair.stat.question__title_slug: True if pair.status == "ac" else False
            for pair in api_response.stat_status_pairs
        }

        #print(slug_to_solved_status)

        #print(len(slug_to_solved_status))

        #count = 0

        data = []

        for slug in slug_to_solved_status:
            
            if slug_to_solved_status[slug] == True:
                
                data.append(slug)
                #count +=1
                #print(slug, slug_to_solved_status[slug])

        return data
        #print("count", count

data = leetclass.get_data()

for i in data:

    print(i)
