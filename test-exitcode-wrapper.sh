spawn pysys run -vINFO
expect {
	"Test final outcome:  PASSED" { exit 0 }
	"Test final outcome:  FAILED" { exit 1 }
	oef { exit 1 }
}