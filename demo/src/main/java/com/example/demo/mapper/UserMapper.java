package com.example.demo.mapper;

import com.example.demo.dom.User;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface UserMapper {
    public List<String> getuser(String username);
    public void adduser(String username,String password);
    public void deleteuser(String username);
}
