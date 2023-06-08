package com.example.demo.controller;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import java.io.*;

@RestController
public class FileController {
    @RequestMapping("/upload")
    public void upload(@RequestParam("file") MultipartFile file, @RequestParam String filename,HttpServletRequest request){
        int n;
        File f = new File("D:\\dbas\\data\\"+filename+".csv");
        try ( InputStream in  = file.getInputStream(); OutputStream os = new FileOutputStream(f)){
            byte[] buffer = new byte[4096];
            while ((n = in.read(buffer,0,4096)) != -1){
                os.write(buffer,0,n);
            }
        }catch (IOException e){
            e.printStackTrace();
        }
    }
    @RequestMapping("/download/{filename}")
    public void download(@PathVariable("filename") String filename, HttpServletResponse response){
        File file = new File("D:\\dbas\\data\\"+filename);
        byte[] buffer = new byte[1024];
        BufferedInputStream bis = null;
        OutputStream os = null;
        try {
            //文件是否存在
            if (file.exists()) {
                //设置响应
                response.setContentType("application/octet-stream;charset=UTF-8");
                response.setCharacterEncoding("UTF-8");
                os = response.getOutputStream();
                bis = new BufferedInputStream(new FileInputStream(file));
                while (bis.read(buffer) != -1) {
                    os.write(buffer);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (bis != null) {
                    bis.close();
                }
                if (os != null) {
                    os.flush();
                    os.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
