using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using Final_Project.Models;


namespace Final_Project.Controllers
{
    public class UsersController : ApiController
    {
        // GET api/<controller>
        public List<User> Get()
        {
            User user = new User();
            return user.ReadAllUsers();
        }

        // GET api/<controller>/5
        public string Get(int id)
        {
            return "value";
        }

        // POST api/<controller>
        public int Post([FromBody] User user)
        {
            return user.InsertUser();
        }

        // PUT api/<controller>/5
        public void Put(int id, [FromBody]string value)
        {
        }

        // DELETE api/<controller>/5
        public string Delete([FromBody] User u)
        {
            return u.UpdateStatus();
        }
    }
}