#!/bin/bash

% free | awk 'FNR == 3 {print $3/($3+$4)*100}'
