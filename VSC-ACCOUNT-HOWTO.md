# How to request an VSC account

This document describes the procedure to request an VSC account.


## Create a public-private key pair

To log on to and use the VSC infrastructure, you need a so-called VSC account.
VSC accounts don't use regular, fixed passwords but rather a key pair consisting of a public and a private key since that is a more secure technique for authentication.

A key pair consists of a private and a public key. The private key is stored on the computer(s) from which you want to access the VSC and always stays there. The public key is stored on the systems you want to access, granting access to the anyone who can prove to have access to the corresponding private key. Therefore it is very important to protect your private key, as anybody who has access to it can access your VSC account. So for extra security, the private key itself should be encrypted using a 'passphrase', to prevent anyone from using your private key, even when they manage to copy it. You have to 'unlock' the private key by typing the passphrase when you use it.

How to generate such a key pair depends on the operating system of your computer. Instructions for Linux, Windows and macOS can be found in the following links:

- [Linux](https://www.vscentrum.be/client/linux/keys-openssh/)
- [Windows](https://www.vscentrum.be/client/windows/keys-putty/)
- [macOS (formerly OS X)](https://www.vscentrum.be/client/macosx/keys-openssh/)


Once you have generated your key pair, you will be able to apply for a VSC account.


## Send an account request

To request your VSC account send an email to the address : hpcinfo@kuleuven.be

- with the subject: *Astrohack account request*;
- attach the public key of the key pair you have generated before;
- specify the email address you want to have associated with the VSC account.


## Forward the activation link to us

Once your VSC account has been created, you will receive an email containing a link to activate your account.
Because the activation link is only accessible from the KU Leuven network, you will have to forward it to us and we will activate the account.
For the activation sent an email to the address : hpcinfo@kuleuven.be
- with the subject: *Astrohack account activation*;
- the content of the activation mail you received.

Once the activation has been done you will be notified by email.


## Test that you can connect to the cluster

The next step will be to verify that you can connect to the VSC cluster. There are two ways to accomplish that.

### Remote Desktop connection

You can use freeware NoMachine NX Client to connect to HPC cluster in the GUI mode. The instructions on how to set up that type of connection can be found on the [NX section](https://www.vscentrum.be/client/multiplatform/nx-start-guide) of the VSC website.

### Command line connection

The connection to the cluster is done via an ssh-client to one of the 2 login nodes:

- login.hpc.kuleuven.be
- login2.hpc.kuleuven.be

The software you'll need to use on your client system depends on its operating system. In the following pages you can find the instructions for Linuc, Windows and macOS:

- [Linux](https://www.vscentrum.be/client/linux)
- [Windows](https://www.vscentrum.be/client/windows#connecting)
- [macOS (formerly OS X)](https://www.vscentrum.be/client/macosx)


## Help

If you need additional or information or help on requesting the VSC account you can contact us: hpcinfo@kuleuven.be
