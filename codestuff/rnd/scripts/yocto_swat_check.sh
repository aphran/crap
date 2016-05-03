#!/usr/bin/env bash

URL='https://autobuilder.yoctoproject.org/main/tgrid'
DEFAULT_BRANCH='master'
FROM='SWAT_Sarge@reports.it'
NAME="${0}"

for arg in "${@}"; do
    if [[ "${arg}" =~ -h$|--help$ ]]; then
        cat << EOF

Simple SWAT build failure checker

    Usage: ${NAME} [-h|--help] [branch] [email]

Checks AutoBuilder tgrid view for failed builds.
The URL is: ${URL}
Default branch is: ${DEFAULT_BRANCH}
If email is included, an email will be sent to that address. Otherwise, no email is sent

EOF
        exit 0
    fi
done

content="$( curl -ks ${URL} | tr -d '\n' | sed 's/[ ]\{1,\}/ /g' )"
branch=${1-${DEFAULT_BRANCH}}
echo "Using branch:  ${branch}"
email=${2-}

pattern="Branch:</b> ${branch} <br/><b>Repo: </b> <a href=\"[a-zA-Z0-9:.=&?_/-]+\"> [a-zA-Z0-9:.=&?_/-]+ </a> <br/><b>Build:</b> <a href=\"[a-zA-Z0-9:.=&?_/-]+\">failed"
#echo "Using pattern: ${pattern}"

match=$(eval "echo '$content' | egrep -o '${pattern}' --color")

status='ALRIGHT'
exitcode=0
if [ -n "${match}" ]; then
    status="FAILED!"
    exitcode=1
fi
echo "Status: ${status}"

if [ -n "${email}" ] && [ ${status} == 'FAILED!' ]; then
    echo "E-mailing report to: ${email}"
    echo -e "The ${NAME} script returned status '${status}' after running at: $(date +%Y-%m-%d_%H:%M:%S)\n\nURL: ${URL}\nBranch: ${branch}\n\nThe returned match was:\n\n${match}\n\n Stern regards,\n - The SWAT Sarge" | mailx -v -r "${FROM}" -s "SWAT AB <${status}> for branch <${branch}>" -S smtp="fm-out.intel.com:25" -S ssl-verify=ignore ${email} &>/dev/null
fi

exit ${exitcode}
