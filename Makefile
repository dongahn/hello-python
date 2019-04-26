all: done

done: test.py
	touch done

check: test.py
	./test.py

clean:
	rm done
