#!/usr/bin/bash

func() {
    for item in "${@}"; do
        echo "${item}"
    done
}

func "${@}"
