for i in range(0,50):
        # Do something
        time.sleep(0.05)
        printProgress(i, 50, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
