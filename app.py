from flask import Flask, request
import paramiko
import json

app = Flask(__name__)


@app.route('/clusters')
def get_all_cluster():
    result = ''
    response = []

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('10.136.65.15', username='root', password='gsLab!23')

    stdin, stdout, stderr = client.exec_command("cloudctl mc get clusters -o json ")
    try:
        for line in stdout:
            str1 = line.strip('\n')
            result +=str1
    except Exception as e:
        print("Token expire. please check login to mcm.")
    
    for key, values in json.loads(result).items():
        
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
    return json.dumps(response)

@app.route('/cluster/<cluster>/pods/<pod_state>')
def get_cluster_pods(cluster, pod_state):
    """
    Get all cluster pods
    i/o params
    cluster name
    state of pod

    o/p params:
    Name: pod name
    Namespaces: namespace
    status: status of pod
    Event: get all pods event
    """

    result = ''
    event = ""
    pod_info= []
    final_response = []
    ## get cluter name and pod status

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('10.136.65.15', username='root', password='gsLab!23')
    stdin, stdout, stderr = client.exec_command("kubectl get pods --all-namespaces -o json")

    for line in stdout:
        str1 = line.strip('\n')
        result +=str1
    for key, value in json.loads(result).items():
        if key == 'items':
            for val in value:
                temp_dict={'name':'', 'namespace':'', 'status':''}
                for k, v in val.items():
                    if k == 'metadata':
                        temp_dict['name'] = v.get('name')
                        temp_dict['namespace']= v.get('namespace')
                    if k == 'status':
                        temp_dict['status']= v.get('phase')
                pod_info.append(temp_dict)
    # stdin, stdout, stderr = client.exec_command("oc describe pod logging-curator-1602453600-f9tm2 -n openshift-logging | grep -A20 Events")
    
    for p_inf in pod_info:

        if p_inf.get('status') != "Running":
            temp_dict1={'name':'', 'namespace':'', 'status':'', 'Event' :[]}

            command= "oc describe pod " +  p_inf.get('name') + " -n " + p_inf.get('namespace') + " | grep -A20 Events"
            stdin, stdout, stderr = client.exec_command(command)
    
            for line in stdout:
                str1 = line.strip('\n')
                event +=str1
            temp_dict1['name']= p_inf.get('name')
            temp_dict1['namespace']= p_inf.get('namespace')
            temp_dict1['status']= p_inf.get('status')
            s= get_event(p_inf.get('name'), p_inf.get('namespace'))
            temp_dict1['Event'] = s
            final_response.append(temp_dict1)
        
    return json.dumps(final_response)

@app.route('/cluster/<cluster>/namespace/<namespace>/pods')
def get_cluster_pods_namespace(cluster, namespace):
    """
    Get all cluster pods
    i/o params
    cluster name
    state of pod

    o/p params:
    Name: pod name
    Namespaces: namespace
    status: status of pod
    Event: get all pods event
    """

    result = ''
    event = ""
    pod_info= []
    final_response = []
    ## get cluter name and pod status

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('10.136.65.15', username='root', password='gsLab!23')
    command1 = "kubectl get pods -n "+ namespace+" -o json"
    stdin, stdout, stderr = client.exec_command(command1)

    for line in stdout:
        str1 = line.strip('\n')
        result +=str1
    for key, value in json.loads(result).items():
        if key == 'items':
            for val in value:
                temp_dict={'name':'', 'namespace':'', 'status':''}
                for k, v in val.items():
                    if k == 'metadata':
                        temp_dict['name'] = v.get('name')
                        temp_dict['namespace']= v.get('namespace')
                    if k == 'status':
                        temp_dict['status']= v.get('phase')
                pod_info.append(temp_dict)
    
    for p_inf in pod_info:

            temp_dict1={'name':'', 'namespace':'', 'status':'', 'Event' :[]}

            command= "oc describe pod " +  p_inf.get('name') + " -n " + p_inf.get('namespace') + " | grep -A20 Events"
            stdin, stdout, stderr = client.exec_command(command)
    
            for line in stdout:
                str1 = line.strip('\n')
                event +=str1
            temp_dict1['name']= p_inf.get('name')
            temp_dict1['namespace']= p_inf.get('namespace')
            temp_dict1['status']= p_inf.get('status')
            s= get_event(p_inf.get('name'), p_inf.get('namespace'))
            temp_dict1['Event'] = s
            final_response.append(temp_dict1)
        
    return json.dumps(final_response)


def get_event(pod_name, namespace): 
    '''
    Funtion to get Event on the basis of pod name and it's namespaces
    i/p params: pod_name,namespace
    o/p params: Message, Reason, Type
    '''
    event =""
    event_list=[]
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('10.136.65.15', username='root', password='gsLab!23')
    stdin, stdout, stderr = client.exec_command("kubectl get pods --all-namespaces -o json")
    command = "kubectl get events --field-selector=involvedObject.name=" +pod_name + ' -n '+ namespace +" -o json"
    stdin, stdout, stderr = client.exec_command(command)
    for line in stdout:
        str1 = line.strip('\n')
        event +=str1
 
    temp = json.loads(event)
    for key, value in temp.items():
        if key == 'items':
            for val in value:
                temp_dict={'Message':'', 'Reason':'', 'Type':''}
                temp_dict['Message']=val.get('message')
                temp_dict['Reason']=val.get('reason')
                temp_dict['Type']=val.get('type')
                event_list.append(temp_dict)

    return event_list


if __name__ == "__main__":
    app.run()