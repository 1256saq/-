package com.example.demo.controller;

import com.alibaba.fastjson.JSON;
import com.example.demo.dom.tbcell;
import com.example.demo.mapper.TbcellMapper;
import com.example.demo.service.TbcellService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class QueryController {
    @Autowired
    TbcellService tbcellService;
    @RequestMapping("/allsector")
    public List<String> getsectors(){
        return tbcellService.SECTORS();
    }
    @RequestMapping("/tbcell")
    public String gettbcell(String SECTOR_ID){
        System.out.println(JSON.toJSONString(tbcellService.gettbcell(SECTOR_ID)));
        return JSON.toJSONString(tbcellService.gettbcell(SECTOR_ID));
    }
    @RequestMapping("/enodeb")
    public String getenodebcell(String ENODEB_ID){
        System.out.println(ENODEB_ID);
        System.out.println(JSON.toJSONString(tbcellService.gettbenodeb(ENODEB_ID)));
        return JSON.toJSONString(tbcellService.gettbenodeb(ENODEB_ID));
    }
    @RequestMapping("/allenodeb")
    public List<String> getenodebs(){
        return tbcellService.ENODEBS();
    }
    @RequestMapping("/kpipaint")
    public void kpipaint(String SECTOR_NAME,String NODE_NAME,String START_TIME,String END_TIME){
        System.out.println(SECTOR_NAME);
        System.out.println(NODE_NAME);
        System.out.println(START_TIME);
        System.out.println(END_TIME);
    }
}
