cd test
spawn pysys run -vINFO
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