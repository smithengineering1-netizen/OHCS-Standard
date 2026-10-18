import scipy.io as sio

report = sio.loadmat('report.mat')['report']

if report['overall_pass'][0][0]:
    print("CONFORMANCE: PASS")
    exit(0)
else:
    print("CONFORMANCE: FAIL")
    exit(1)
