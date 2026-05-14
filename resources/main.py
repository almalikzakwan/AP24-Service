# This is from my POV using Apache24, All developments config will be on conf/extra/developments folder, which will set by 
# include <example.conf> in conf/extra/httpd-vhosts.conf file. We need to change every port listed in the vhost file.
# in my perpective in learning Apache24 , we also need to change to custom used port in httpd.conf and httpd-ssl.conf
#
# Example usage

# i will configure random default and ssl port using example below in init() function.
from functions.init import kickoff as main

# initialization of script    
main.kickoff()