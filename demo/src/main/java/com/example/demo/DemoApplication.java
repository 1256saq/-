package com.example.demo;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@MapperScan("com.example.demo.mapper")
@SpringBootApplication
public class DemoApplication {
//    @Value ( "${spring.application.name}" )
//    String appName;
//
//    private static Logger logger = LoggerFactory.getLogger ( ExampleRestartApplication.class );
//
//    private static String[] args;
//    private static ConfigurableApplicationContext context;
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
//    @GetMapping("/refresh")
//    public String restart(){
//        logger.info ( "spring.application.name:"+appName);
//        try {
//            PropUtil.init ().write ( "spring.application.name","SPRING-DYNAMIC-SERVER" );
//        } catch (IOException e) {
//            e.printStackTrace ( );
//        }
//
//        ExecutorService threadPool = new ThreadPoolExecutor (1,1,0, TimeUnit.SECONDS,new ArrayBlockingQueue<> ( 1 ),new ThreadPoolExecutor.DiscardOldestPolicy ());
//        threadPool.execute (()->{
//            context.close ();
//            context = SpringApplication.run ( ExampleRestartApplication.class,args );
//        } );
//        threadPool.shutdown ();
//        return "spring.application.name:"+appName;
//    }
//
//    @GetMapping("/info")
//    public String info(){
//        logger.info ( "spring.application.name:"+appName);
//        return appName;
//    }

}
