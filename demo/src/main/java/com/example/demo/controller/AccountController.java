package com.example.demo.controller;

import com.example.demo.dom.User;
import com.example.demo.service.ManagerService;
import com.example.demo.service.UserService;
import org.apache.catalina.valves.JsonAccessLogValve;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;

import java.util.ArrayList;
import java.util.List;
import java.util.SplittableRandom;

@RestController
public class AccountController {
    @Autowired
    ManagerService managerService;
    @Autowired
    UserService userService;
    @RequestMapping("/userlogin")
    public String userlogin(@RequestParam String username,@RequestParam String password){
        if(userService.Login(username,password)){
            return "TRUE";
        }
        return "FALSE";
    }
    @RequestMapping("/managerlogin")
    public String managerlogin(@RequestParam String username,@RequestParam String password){
        return "TRUE";
    }
    @RequestMapping("/deleteuser")
    public void deleteuser(@RequestParam String username){
        userService.deleteuser(username);
    }
    @RequestMapping("/alluser")
    public String alluser(){
        System.out.println(JSON.toJSONString(managerService.alluser()));
        return JSON.toJSONString(managerService.alluser());
    }
    @RequestMapping("/adduser")
    public void adduser(@RequestParam String username,@RequestParam String password){
        managerService.adduser(username,password);
    }
    @RequestMapping("/dbasmanage")
    public void dbasmanage(@RequestParam String url,@RequestParam String name,@RequestParam String password,@RequestParam String driverclassname){
        System.out.println(url);
        System.out.println(name);
        System.out.println(password);
        System.out.println(driverclassname);
    }
}
