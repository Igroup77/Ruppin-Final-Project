﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using Final_Project.Models;

namespace Final_Project.Controllers
{
    public class RightsController : ApiController
    {
        // GET api/<controller>
        public List <Right> Get()
        {
            Right right = new Right();
            return right.ReadAllRights();
        }

        // GET api/<controller>/5
        public int Get(int some)
        {
            Right right = new Right();
            return right.ReadcountRights();
        }


        // POST api/<controller>
        public object Post([FromBody] Right right)
        {
            return right.InsertRight();
        }



        // PUT api/<controller>/5
        public void Put(int id, [FromBody]string value)
        {
        }

        // DELETE api/<controller>/5
        public string Delete([FromBody] Right r)
        {
            return r.UpdateStatus();
        }
    }
}