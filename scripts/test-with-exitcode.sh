#!/usr/bin/expect -f

cd test
spawn pysys run -v INFO 
log_user 0
expect "INFO  ======="
log_user 1
expect {
	"Test final outcome:  PASSED" { 
		expect eof
		exit 0 
	}
	"Test final outcome:  FAILED" { 
		expect eof 
		exit 1 
	}
	oef { exit 1 }
}