# kubernetes-Api

This Python script configures Kubernetes pods based on data retrieved from a calendar API. It checks whether it's a maintenance day, and if it is, blocks access to the cluster. If it's not a maintenance day, it allows access from specific cities. It also checks the calendar API to see if the pods should be scaled today, and if so, scales them up by one pod. It utilizes the Kubernetes API client library and the requests library to interact with the external calendar API.
