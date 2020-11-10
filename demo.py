import json
def sample(result):
    response = []
    for key, values in result.items():
        if key == 'items':
            for value in values:
                temp_dict={'name':'', 'namespace':'', 'status':''}
                for k, v in value.items():
                    # and v.get('conditions')[0].get('type') == "OK"
                    if k == 'status' and not bool(v) :
                        temp_dict['status'] = "Pending"
                    elif k == 'status' and v.get('conditions')[0].get('type') == "OK":
                        temp_dict['status'] = "Offline"
                    elif k == 'status' and v.get('conditions')[0].get('type') == "":
                        temp_dict['status'] = "Ready"
                
                    if k == 'metadata':
                        temp_dict['name'] = v.get('name')
                        temp_dict['namespace'] = v.get('namespace')
                response.append(temp_dict)
    return response



result = {
   "kind":"List",
   "apiVersion":"v1",
   "metadata":{
      
   },
   "items":[
      {
         "kind":"Cluster",
         "apiVersion":"clusterregistry.k8s.io/v1alpha1",
         "metadata":{
            "name":"demo-cluster",
            "namespace":"demo-cluster",
            "selfLink":"/apis/clusterregistry.k8s.io/v1alpha1/namespaces/demo-cluster/clusters/demo-cluster",
            "uid":"dbe14b90-1e60-11eb-a108-0a580a830059",
            "resourceVersion":"18720",
            "creationTimestamp":"2020-11-04T05:44:51Z",
            "labels":{
               "cloud":"auto-detect",
               "vendor":"auto-detect"
            },
            "annotations":{
               "mcm.ibm.com/user-group":"c3lzdGVtOnNlcnZpY2VhY2NvdW50cyxzeXN0ZW06c2VydmljZWFjY291bnRzOmt1YmUtc3lzdGVtLHN5c3RlbTphdXRoZW50aWNhdGVk",
               "mcm.ibm.com/user-identity":"c3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmUtc3lzdGVtOmRlZmF1bHQ=",
               "seed-generation":"1"
            },
            "finalizers":[
               "rcm-api.cluster",
               "propagator.finalizer.mcm.ibm.com"
            ]
         },
         "spec":{
            "kubernetesApiEndpoints":{
               
            },
            "authInfo":{
               
            }
         },
         "status":{
            
         }
      },
      {
         "kind":"Cluster",
         "apiVersion":"clusterregistry.k8s.io/v1alpha1",
         "metadata":{
            "name":"local-cluster-gurj",
            "namespace":"local-cluster-gurj",
            "selfLink":"/apis/clusterregistry.k8s.io/v1alpha1/namespaces/local-cluster-gurj/clusters/local-cluster-gurj",
            "uid":"04dc5409-225d-11eb-a108-0a580a830059",
            "resourceVersion":"46522",
            "creationTimestamp":"2020-11-09T07:27:27Z",
            "labels":{
               "cloud":"auto-detect",
               "vendor":"auto-detect"
            },
            "annotations":{
               "mcm.ibm.com/user-group":"c3lzdGVtOnNlcnZpY2VhY2NvdW50cyxzeXN0ZW06c2VydmljZWFjY291bnRzOmt1YmUtc3lzdGVtLHN5c3RlbTphdXRoZW50aWNhdGVk",
               "mcm.ibm.com/user-identity":"c3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmUtc3lzdGVtOmRlZmF1bHQ=",
               "seed-generation":"1"
            },
            "finalizers":[
               "rcm-api.cluster",
               "propagator.finalizer.mcm.ibm.com"
            ]
         },
         "spec":{
            "kubernetesApiEndpoints":{
               
            },
            "authInfo":{
               
            }
         },
         "status":{
            
         }
      },
      {
         "kind":"Cluster",
         "apiVersion":"clusterregistry.k8s.io/v1alpha1",
         "metadata":{
            "name":"local-cluster-pooja",
            "namespace":"local-cluster-pooja",
            "selfLink":"/apis/clusterregistry.k8s.io/v1alpha1/namespaces/local-cluster-pooja/clusters/local-cluster-pooja",
            "uid":"cb55c299-225a-11eb-a108-0a580a830059",
            "resourceVersion":"47766",
            "creationTimestamp":"2020-11-09T07:11:31Z",
            "labels":{
               "cloud":"Other",
               "name":"local-cluster-pooja",
               "vendor":"Other"
            },
            "annotations":{
               "mcm.ibm.com/hub":"hub0",
               "mcm.ibm.com/user-group":"c3lzdGVtOnNlcnZpY2VhY2NvdW50cyxzeXN0ZW06c2VydmljZWFjY291bnRzOmt1YmUtc3lzdGVtLHN5c3RlbTphdXRoZW50aWNhdGVk",
               "mcm.ibm.com/user-identity":"c3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmUtc3lzdGVtOmRlZmF1bHQ=",
               "seed-generation":"2"
            },
            "finalizers":[
               "rcm-api.cluster",
               "propagator.finalizer.mcm.ibm.com"
            ]
         },
         "spec":{
            "kubernetesApiEndpoints":{
               "serverEndpoints":[
                  {
                     "clientCIDR":"0.0.0.0/0",
                     "serverAddress":"10.0.2.15:8443"
                  }
               ]
            },
            "authInfo":{
               
            }
         },
         "status":{
            "conditions":[
               {
                  "type":"",
                  "status":"",
                  "lastHeartbeatTime":"2020-11-09T11:49:23Z",
                  "lastTransitionTime":"2020-11-09T11:50:54Z",
                  "reason":"Klusterlet failed to update cluster status on time"
               }
            ]
         }
      },
      {
         "kind":"Cluster",
         "apiVersion":"clusterregistry.k8s.io/v1alpha1",
         "metadata":{
            "name":"local-gurjeet-cluster",
            "namespace":"local-gurjeet-cluster",
            "selfLink":"/apis/clusterregistry.k8s.io/v1alpha1/namespaces/local-gurjeet-cluster/clusters/local-gurjeet-cluster",
            "uid":"ed9a2198-226d-11eb-a108-0a580a830059",
            "resourceVersion":"47101",
            "creationTimestamp":"2020-11-09T09:28:29Z",
            "labels":{
               "cloud":"Other",
               "name":"local-gurjeet-cluster",
               "vendor":"Other"
            },
            "annotations":{
               "mcm.ibm.com/hub":"hub0",
               "mcm.ibm.com/user-group":"c3lzdGVtOnNlcnZpY2VhY2NvdW50cyxzeXN0ZW06c2VydmljZWFjY291bnRzOmt1YmUtc3lzdGVtLHN5c3RlbTphdXRoZW50aWNhdGVk",
               "mcm.ibm.com/user-identity":"c3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmUtc3lzdGVtOmRlZmF1bHQ=",
               "seed-generation":"2"
            },
            "finalizers":[
               "rcm-api.cluster",
               "propagator.finalizer.mcm.ibm.com"
            ]
         },
         "spec":{
            "kubernetesApiEndpoints":{
               "serverEndpoints":[
                  {
                     "clientCIDR":"0.0.0.0/0",
                     "serverAddress":"10.0.2.15:8443"
                  }
               ]
            },
            "authInfo":{
               
            }
         },
         "status":{
            "conditions":[
               {
                  "type":"",
                  "status":"",
                  "lastHeartbeatTime":"2020-11-09T09:52:25Z",
                  "lastTransitionTime":"2020-11-09T09:53:54Z",
                  "reason":"Klusterlet failed to update cluster status on time"
               }
            ]
         }
      },
      {
         "kind":"Cluster",
         "apiVersion":"clusterregistry.k8s.io/v1alpha1",
         "metadata":{
            "name":"mcm-cluster",
            "namespace":"mcm-cluster",
            "selfLink":"/apis/clusterregistry.k8s.io/v1alpha1/namespaces/mcm-cluster/clusters/mcm-cluster",
            "uid":"960ad9ea-1ce4-11eb-a108-0a580a830059",
            "resourceVersion":"49088",
            "creationTimestamp":"2020-11-02T08:22:46Z",
            "labels":{
               "cloud":"Other",
               "env":"dev",
               "name":"mcm-cluster",
               "vendor":"Other"
            },
            "annotations":{
               "mcm.ibm.com/hub":"hub0",
               "mcm.ibm.com/user-group":"aGNtOmNsdXN0ZXJzLHN5c3RlbTphdXRoZW50aWNhdGVk",
               "mcm.ibm.com/user-identity":"aGNtOmNsdXN0ZXJzOm1jbS1jbHVzdGVyOm1jbS1jbHVzdGVy",
               "seed-generation":"2"
            },
            "finalizers":[
               "rcm-api.cluster",
               "propagator.finalizer.mcm.ibm.com"
            ]
         },
         "spec":{
            "kubernetesApiEndpoints":{
               "serverEndpoints":[
                  {
                     "clientCIDR":"0.0.0.0/0",
                     "serverAddress":"10.0.2.15:8443"
                  }
               ]
            },
            "authInfo":{
               
            }
         },
         "status":{
            "conditions":[
               {
                  "type":"OK",
                  "status":"",
                  "lastHeartbeatTime":"2020-11-09T18:05:18Z",
                  "lastTransitionTime":'null'
               }
            ]
         }
      },
      {
         "kind":"Cluster",
         "apiVersion":"clusterregistry.k8s.io/v1alpha1",
         "metadata":{
            "name":"new-minishift-cluster-in-lab",
            "namespace":"new-minishift-cluster-in-lab",
            "selfLink":"/apis/clusterregistry.k8s.io/v1alpha1/namespaces/new-minishift-cluster-in-lab/clusters/new-minishift-cluster-in-lab",
            "uid":"fa5e2b11-18ee-11eb-a108-0a580a830059",
            "resourceVersion":"1810",
            "creationTimestamp":"2020-10-28T07:27:04Z",
            "labels":{
               "cloud":"auto-detect",
               "vendor":"auto-detect"
            },
            "annotations":{
               "mcm.ibm.com/user-group":"c3lzdGVtOnNlcnZpY2VhY2NvdW50cyxzeXN0ZW06c2VydmljZWFjY291bnRzOmt1YmUtc3lzdGVtLHN5c3RlbTphdXRoZW50aWNhdGVk",
               "mcm.ibm.com/user-identity":"c3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmUtc3lzdGVtOmRlZmF1bHQ=",
               "seed-generation":"1"
            },
            "finalizers":[
               "rcm-api.cluster",
               "propagator.finalizer.mcm.ibm.com"
            ]
         },
         "spec":{
            "kubernetesApiEndpoints":{
               
            },
            "authInfo":{
               
            }
         },
         "status":{
            
         }
      },
      {
         "kind":"Cluster",
         "apiVersion":"clusterregistry.k8s.io/v1alpha1",
         "metadata":{
            "name":"temp",
            "namespace":"temp",
            "selfLink":"/apis/clusterregistry.k8s.io/v1alpha1/namespaces/temp/clusters/temp",
            "uid":"baad7be3-19d3-11eb-a108-0a580a830059",
            "resourceVersion":"3204",
            "creationTimestamp":"2020-10-29T10:44:32Z",
            "labels":{
               "cloud":"auto-detect",
               "vendor":"auto-detect"
            },
            "annotations":{
               "mcm.ibm.com/user-group":"c3lzdGVtOnNlcnZpY2VhY2NvdW50cyxzeXN0ZW06c2VydmljZWFjY291bnRzOmt1YmUtc3lzdGVtLHN5c3RlbTphdXRoZW50aWNhdGVk",
               "mcm.ibm.com/user-identity":"c3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmUtc3lzdGVtOmRlZmF1bHQ=",
               "seed-generation":"1"
            },
            "finalizers":[
               "rcm-api.cluster",
               "propagator.finalizer.mcm.ibm.com"
            ]
         },
         "spec":{
            "kubernetesApiEndpoints":{
               
            },
            "authInfo":{
               
            }
         },
         "status":{
            
         }
      },
      {
         "kind":"Cluster",
         "apiVersion":"clusterregistry.k8s.io/v1alpha1",
         "metadata":{
            "name":"test-c",
            "namespace":"test-c",
            "selfLink":"/apis/clusterregistry.k8s.io/v1alpha1/namespaces/test-c/clusters/test-c",
            "uid":"844e9c2d-227b-11eb-a108-0a580a830059",
            "resourceVersion":"47497",
            "creationTimestamp":"2020-11-09T11:05:46Z",
            "labels":{
               "cloud":"auto-detect",
               "vendor":"auto-detect"
            },
            "annotations":{
               "mcm.ibm.com/user-group":"c3lzdGVtOnNlcnZpY2VhY2NvdW50cyxzeXN0ZW06c2VydmljZWFjY291bnRzOmt1YmUtc3lzdGVtLHN5c3RlbTphdXRoZW50aWNhdGVk",
               "mcm.ibm.com/user-identity":"c3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmUtc3lzdGVtOmRlZmF1bHQ=",
               "seed-generation":"1"
            },
            "finalizers":[
               "rcm-api.cluster",
               "propagator.finalizer.mcm.ibm.com"
            ]
         },
         "spec":{
            "kubernetesApiEndpoints":{
               
            },
            "authInfo":{
               
            }
         },
         "status":{
            
         }
      }
   ]
}

print(sample(result))