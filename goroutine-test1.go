//对比程序，系统发生1亿次并发，并发为一个无操作的空函数，使用time指令对比性能
package main

import (
	"runtime"
	"fmt"
	"time"
)

const (
	TIMES = 100 * 1000 * 100
)

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())
	fmt.Println("CPUs:", runtime.NumCPU(), "Goroutines:", runtime.NumGoroutine())
	t1 := time.Now()
	for i:=0; i<TIMES; i++ {
		go func() {}()
	}

	for runtime.NumGoroutine() > 4 {
		//fmt.Println("current goroutines:", runtime.NumGoroutine())
		//time.Sleep(time.Second)
	}
	t2 := time.Now()
	fmt.Printf("elapsed time: %.3fs\n", t2.Sub(t1).Seconds())
}

/*
————————————————
版权声明：本文为CSDN博主「anteoy」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/yan_chou/article/details/65633658
*/


