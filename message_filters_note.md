1. 相同的模式
	- FooFilter foo;
	- BarFilter bar;
	- 输入通过构造函数或者connectInput( )连接
		- bar.connectInput(foo);
	- 输出通过registerCallback( )连接
		- bar.registerCallback(myCallback);

2. Subscriber
	- message_filters::Subscriber<std_msgs::UInt32>sub(nh,"my_topic",1);
	- sub.registerCallback(myCallback);

	- which is equivalent of 

	- ros::Subscriber sub = nh.subscribe("my_topic",1,myCallback);
3. 时间同步器(Time Synchronizer)
	- TimeSynchronizer过滤器通过head中包含的时间戳同步传入，并采用相同数量的单个回调的形式输出，最多9个通道


