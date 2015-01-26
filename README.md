# twcswiftclient
Storing Images &amp; Videos to Openstack Cloud Storage using Swift Client


##Installation Steps:

**1. Pull the code from Repo :**

git clone https://github.com/gopal1cloud/twcswiftclient.git

**2. Get into Project Folder :**

$ cd twcswiftclient/

**3. Install Dependencies from requirement file :**

$ pip install -r requirement.txt 


**4. Modify Openstack Cloud configuration on settings file :**

$ vim twcswiftclient/settings.py

## Configuring
django-storage-swift recognises the following options from settings file.

| Option | Default | Description |
| ------ | ------- | ----------- |
| ```SWIFT_AUTH_URL``` | None | The URL for the auth server, e.g. ```http://127.0.0.1:5000/v2.0``` |
| ```SWIFT_USERNAME``` | None | The username to use to authenticate. |
| ```SWIFT_KEY``` | None | The key (password) to use to authenticate. |
| ```SWIFT_AUTH_VERSION``` | 1 | The version of the authentication protocol to use. |
| ```SWIFT_TENANT_NAME``` | None | The tenant name to use when authenticating. |
| ```SWIFT_CONTAINER_NAME``` | None | The container in which to store the files. |
| ```SWIFT_STATIC_CONTAINER_NAME``` | None | Alternate container used by StaticSwiftStorage. |
| ```SWIFT_AUTO_CREATE_CONTAINER``` | False | Should the container be created if it does not exist? |
| ```SWIFT_AUTO_BASE_URL``` | True | Query the authentication server for the base URL. |
| ```SWIFT_BASE_URL``` | None | The base URL from which the files can be retrieved, e.g. ```http://127.0.0.1:8080/```.  |
| ```SWIFT_USE_TEMP_URLS``` | False | Generate temporary URLs for file access (allows files to be accessed without a permissive ACL). |
| ```SWIFT_TEMP_URL_KEY``` | None | Temporary URL key --- see [the OpenStack documentation][openstack-tempurl]. |
| ```SWIFT_TEMP_URL_DURATION``` | ```30*60``` | How long a temporary URL remains valid, in seconds. |
| ```SWIFT_EXTRA_OPTIONS``` | ```{}``` | Extra options, eg. { "endpoint_type": "adminURL"  }, which will return adminURL instead publicURL. | 

### SWIFT_BASE_URL
django-swift-storage will automatically query the authentication server for the URL where your files can be accessed, which takes the form ```http://server:port/v1/AUTH_token/```.

Sometimes you want to override the server and port (for example if you're developing using [devstack][devstack] inside Vagrant). This can be accomplished with ```SWIFT_BASE_URL```.

The provided value is parsed, and:

 + host and port override any automatically derived values
 + any path component is put before derived path components.

So if your auth server returns ```http://10.0.2.2:8080/v1/AUTH_012345abcd/``` and you have ```SWIFT_BASE_URL="http://127.0.0.1:8888/foo"```, the ```url``` function will a path based on ```http://127.0.0.1:8888/foo/v1/AUTH_012345abcd/```.

### Temporary URLs

Temporary URLs provide a means to grant a user permission to access a file for a limited time only and without making the entire container public.

Temporary URLs work as described in the Swift documentation. (The code to generate the signatures is heavily based on their implementation.) They require setup of a key for signing: the process is described in [the OpenStack documentation][openstack-tempurl].

**5. Creating Tables on the Database with syncdb command :**

$ python manage.py syncdb

While running Syncdb first time,
(Django auth system asks for the Superusers:)

You have installed Django's auth system, and don't have any superusers defined.

Would you like to create one now? (yes/no): yes

Username (leave blank to use 'admin'): admin

Email address: admin@demo.com

Password: *****

Password (again): *****

**6. Collecting static media files to server :**

$ python manage.py collectstatic

This will overwrite existing files!
Are you sure you want to do this?

Type 'yes' to continue, or 'no' to cancel: yes

**7. Running Django Development Server :**

$ python manage.py runserver

**8. Access the development server specifying the IP in the browser:**

http://127.0.0.1:8000/  

Thats it!!
