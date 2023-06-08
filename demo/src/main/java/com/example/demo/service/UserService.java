package com.example.demo.service;

import com.alibaba.fastjson.JSON;
import com.example.demo.dom.User;
import com.example.demo.mapper.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.List;
@Service
public class UserService {
    @Autowired
    UserMapper mapper;
    public Boolean Login(String name,String password){
        List<String> result=mapper.getuser(name);
        return password.equals(result.get(0));
    }
    public void deleteuser(String name){
        mapper.deleteuser(name);
    }
}
