package com.example.demo.service;

import com.example.demo.dom.User;
import com.example.demo.mapper.ManagerMapper;
import com.example.demo.mapper.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ManagerService {
    @Autowired
    ManagerMapper managerMapper;
    @Autowired
    UserMapper userMapper;
    public void adduser(String username,String password){
        userMapper.adduser(username,password);
    }
    public List<User> alluser(){
        return managerMapper.getalluser();
    }
}
