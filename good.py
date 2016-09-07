import parseCookie
import AutoAttaka


if __name__ == "__main__":
    
    
    
    cookie = "CNZZDATA3458012=cnzz_eid%3D1068221846-1472627900-http%253A%252F%252Fwww.scholat.com%252F%26ntime%3D1473170900; JSESSIONID=868B8476A5201177B32B5357EBF0AA4B"
    
    cookies= parseCookie.parseCookie(cookie)
    
    AutoAttaka.AutoAttaka.establishSender(cookies)
    
    AutoAttaka.AutoAttaka.Mail("fucz")