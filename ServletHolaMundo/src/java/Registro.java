/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
//Se encarga del objeto para la conexión con la bd
import java.sql.Connection;
import java.sql.DriverManager;
//Se encarga de realizar las sentencias sql como son:
import java.sql.Statement;
//Se encarga de generar un objeto para poder realizar las consultas sql
import java.sql.ResultSet;
import javax.servlet.ServletConfig;

/**
 *
 * @author jp999
 */
@WebServlet(urlPatterns = {"/Registro"})
public class Registro extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    
    //variables globales
    private Connection con;
    private Statement set;
    private ResultSet rs;
    
    //constructor
    public void init(ServletConfig cfg) throws ServletException{
        
        //De esta manera se conecta a la bd
        String url /*= "jdbc:mysql:3306//localhost/registro4iv9"*/;
                                //tipodriver:gestorbd:puerto//ip/nombrebd
                       
        //String userName = "root";
        //String password = "pollito2";
         
         try{
             
             Class.forName("com.mysql.jdbc.Driver");
             /*
             A veces el tipo de driver ya viene incluido el puerto de comunicación, es por ello que nos arroja un error de conexión,
             para resolver este error simplemente hacemos lo siguiente:
             
             url = "jdbc:mysql://localhost/registro4iv9";
             
             */
             url = "jdbc:mysql://localhost/registro4iv9";
            con = (Connection) DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/registro4iv9?useSSL=false", "root", "pollito2");


             set = con.createStatement();
             
             System.out.println("Conexión exitosa");
             
         }catch(Exception e){
             System.out.println("Conexión no exitosa");
             System.out.println(e.getMessage());
             System.out.println(e.getStackTrace());
         }
        
    }
    
    
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            
            String nom, appat, apmat, correo, ip, ipr;
            int edad, puerto, puertor;
            
            nom = request.getParameter("nombre");
            appat = request.getParameter("appat");
            apmat = request.getParameter("apmat");
            edad = Integer.parseInt(request.getParameter("edad"));
            correo = request.getParameter("correo");
            
            ip = request.getLocalAddr();
            puerto = request.getLocalPort();
            
            ipr = request.getRemoteAddr();
            puertor = request.getRemotePort();
            
            //vamos a intentar registra en la bd
            try{
                /*
                Para poder registrar un usuario es necesario la sentencia insert bajo el siguiente esquema:
                insert into nombretabla (atributo1, atributo2,...) values ("valor1","valor2",...)
                
                ""son para valores tipo cadena
                ''numerico
                nada numerico
                */
                
                String q = "insert into mregistro (nom_usu, appat_usu, apmat_usu, edad_usu, email_usu) "
                                    +"values "
                                    +"('"+nom+"', '"+appat+"', '"+apmat+"', "+edad+", '"+correo+"')";
                
                set.executeUpdate(q);
                System.out.println("Registro exitoso en la tabla");
                
            out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Servlet Registro</title>");            
            out.println("</head>");
            out.println("<body>");
            out.println("<br>"
                            + "Tu nombre es: "+nom
                            + "<br>"
                            + "Tu apellido paterno es: "+appat
                            + "<br>"
                            + "Tu apellido materno es: "+apmat
                            + "<br>"
                            + "Tu edad es:"+edad
                            + "<br>"
                            + "Tu email es: "+correo
                            +"<br>"
                            +"Tu ip local es: "+ip
                            +"<br>"
                            +"Tu puerto local es"+puerto
                            +"<br>"
                            +"Tu ip remota"+ipr
                            +"<br>"
                            +"Tu puerto remoto es"+puertor);
            out.println("<h1>Registro Exitoso</h1>"
                                + "<a href='index.html'>Regresar al Menu Principal</a>");
            out.println("</body>");
            out.println("</html>");
            }catch(Exception e){
                System.out.println("Error al registrar en la tabla");
                System.out.println(e.getMessage());
                System.out.println(e.getStackTrace());
                
                out.println("<!DOCTYPE html>");
                out.println("<html>");
                out.println("<head>");
                out.println("<title>Servlet Registro</title>");            
                out.println("</head>");
                out.println("<body>");
                 out.println("<h1>Registro no Exitoso, ocurrió un error</h1>"
                                + "<a href='index.html'>Regresar al Menu Principal</a>");
                out.println("</body>");
                out.println("</html>");
            }
            
        }
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
