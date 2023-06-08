package com.example.demo.mapper;

import com.example.demo.dom.User;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface ManagerMapper {
    public List<String> getmanager(String username);
    public List<User> getalluser();
}
