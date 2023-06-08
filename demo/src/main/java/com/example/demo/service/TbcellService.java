package com.example.demo.service;

import com.alibaba.fastjson.JSON;
import com.example.demo.dom.tbcell;
import com.example.demo.mapper.TbcellMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TbcellService {
    @Autowired
    TbcellMapper tbcellMapper;
    public List<String> SECTORS(){
        return tbcellMapper.getallcell();
    }
    public List<tbcell> gettbcell(String SECTOR_ID){
        List<tbcell> ans=tbcellMapper.gettbcell(SECTOR_ID);
        System.out.println(ans.get(0).getCITY());
        return ans;
    }
    public List<String> ENODEBS(){
        return tbcellMapper.getallenodeb();
    }
    public List<tbcell> gettbenodeb(String ENODEB_ID){
        return tbcellMapper.gettbenodeb(ENODEB_ID);
    }
}
