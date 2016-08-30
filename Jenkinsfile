node('agent'){
  def k8s_namespace = readFile '/var/run/secrets/kubernetes.io/serviceaccount/namespace'
  
  stage 'Checkout Code'
  checkout scm
  
  stage 'Prepare Deployment'
  sh 'oc login https://kubernetes.default/ --token=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token) --certificate-authority=/run/secrets/kubernetes.io/serviceaccount/ca.crt'
  
  stage 'Build Image'
  echo 'built'

  stage 'Deploy'
  echo 'deployed'
  
  stage 'Test'
  echo 'tested'
  
}
