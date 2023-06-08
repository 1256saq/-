package com.example.demo.mapper;

import com.example.demo.dom.tbcell;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface TbcellMapper {
    public List<String> getallcell();
    public List<tbcell> gettbcell(String SECTOR_ID);
    public List<String> getallenodeb();
    public List<tbcell> gettbenodeb(String ENODEB_ID);
}
