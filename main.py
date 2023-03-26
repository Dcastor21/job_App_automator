import job_apply


def main(site, email, password):
    site = input("input linked in jobs website link: ")
    email = input("enter Linkedin Email: ")
    password = input(" Enter linked in password")
    return site, email, password


if __name__ == '__main__':
    main()
