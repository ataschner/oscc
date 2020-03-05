# oscc
Offline SupportConfig Checker for SUSE Linux Enterprise systems

Do you ever get exposed to supportconfig files from servers that do not have access to update repositories ? 

Or do you find it difficult to relate to patch numbers of updates (not) installed in updates.txt of a supportconfig ?

If so, how do you easily find out if there are pending updates available from SUSE to be installed on the system to make it up to date ?
Exactly - you don’t.

Until now ...

Install the oscc (for Offline SupportConfig Checker) package on a system with access to a local mirror on e.g. a Repository Mirroring Tool (RMT) or Subscription Management Tool (SMT) server.

This package contains a digested cache of the update repositories for the main SUSE Linux Enterprise (SLE) products along with a plain shell script.

When executed against a supportconfig archive, oscc
- detects the SLE products installed
- sets up and updates the "cache" for the applicable repositories
- examines the SLE package versions installed on the system
- checks if each of the packages is up to date
- displays the results to the user

In the config file the URL to the update repositories needs to be defined. It is assumed to be a directory structure provided by an RMT or SMT server and accessible via http, https, nfs or local storage.
