#include<stdio.h>
 #include<stdlib.h>

  struct node
  {
     int data;
     struct node* link;
  };
  struct node* root = NULL;
  int len;
  void append(void);
  void addatbegin(void);
  void addatafter(void);
  int length(void);
  void display(void);
  void deletebegin(void);
  void deletelast(void);
  void deletepos(void);
  void reverse();
  void search();
  void sort();

  void main()
  {
     int ch;
     clrscr();
     while (1)
     {
	 printf("\nSingle Linked List Operation : \n");
	 printf("1.Insert\t");
	 printf("2.Insert at begin\t");
	 printf("3.Insert at Position\t");
	 printf("4.Length\t");
	 printf("5.Display\t");
	 printf("6.Delete from beigin\t");
	 printf("7.Delete last\t");
	 printf("8.Delete from position\t");
	 printf("9.Reverse\t");
	 printf("10.Sort\t");
	 printf("11.Search\t");
	 printf("12.Quit\n");
	 printf("Enter your choice : ");
	 scanf("%d",&ch);

	 switch(ch)
	 {
	    case 1 : append();
		     break;

	    case 2 : addatbegin();
		     break;

	    case 3 : addatafter();
		     break;

	    case 4 : len = length();
		     printf("Length = %d",len);
		     break;

	    case 5 : display();
		     break;

	    case 6 : deletebegin();
		     break;

	    case 7 : deletelast();
		     break;

	    case 8 : deletepos();
		     break;

	    case 9 : reverse();
		     break;

	    case 10 : sort();
		      break;

	    case 11 : search();
		      break;

	    case 12 : exit(1);

	    default : printf("Wrong Choice !");
	 }

     }

 }


 void append()
 {
    struct node* temp;
    temp =(struct node*)malloc(sizeof(struct node));

    printf("Enter Node data :");
    scanf("%d",&temp->data);
    temp->link = NULL;

    if(root == NULL)
	root = temp;
    else
    {
	struct node* p;
	p = root;
	while(p->link!=NULL)
	{
	    p = p->link;
	}
	p->link = temp;
    }

 }


 int length()
 {
    int count = 0;
    struct node* temp;
    temp = root;
    while(temp!=NULL)
    {
	count++;
	temp=temp->link;
    }
    return count;

 }

 void display()
 {
    struct node* temp,p;
    temp = root;

    if(temp == NULL)
    {
	printf("NO nodes to display \n");
    }

    else
    {
       while(temp!=NULL)
       {
	   printf("%d --> ",temp->data);
	   temp=temp->link;
       }
       printf("\n\n");
    }

 }

  void addatbegin()
  {
    struct node* temp;
    temp =(struct node*)malloc(sizeof(struct node));

    printf("\nEnter Node data to be inserted at first:");
    scanf("%d",&temp->data);
    temp->link = NULL;

    if (root == NULL)
	root=temp;
    else
    {
	temp->link=root;
	root=temp;

    }
  }

  void addatafter()
  {
    struct node *temp,*p;
    int pos,i;
    temp =(struct node*)malloc(sizeof(struct node));
    printf("\nEnter the position :");
    scanf("%d",&pos);
    printf("\nEnter Node data: ");
    scanf("%d",&temp->data);
    temp->link = NULL;

    p = root;
    for(i=0;i<pos-2;i++)
    {
       p = p->link;
    }
    temp->link = p->link;
    p->link=temp;

  }


  void deletebegin()
  {
  struct node *p;
      p=root;
      root=root->link;
      printf("Deleted item = %d\n",p->data);
      free(p);
  }

  void deletelast()
    {
	struct node *ptr,*ptr1;
	if(root == NULL)
	{
	    printf("\nlist is empty");
	}
	else if(root ->link == NULL)
	{
	    root = NULL;
	    free(root);
	    printf("\nOnly node of the list deleted ...");
	}

	else
	{
	    ptr = root;
	    while(ptr->link != NULL)
		{
		    ptr1 = ptr;
		    ptr = ptr ->link;
		}
		ptr1->link = NULL;
		free(ptr);
		printf("\n Deleted Node from the last ...");
	    }
	}
  void deletepos()
  {
      struct node *temp,*p;
      int pos,i;
      printf("Enter position for deletrion : ");
      scanf("%d",&pos);
      if(pos==0)
      {
	 p=root;
	 root=root->link;
	 free(p);
      }
      else
      {
	 p = root;
	 for(i=0;i<pos;i++)
	 {
	     temp=p;
	     p=p->link;
	 }
	 temp->link = p->link;
	 free(p);

      }

  }
  void search()
  {
    struct node *temp=NULL;
    int pos=1,data;
    temp = root;
    printf("Enter data to search :");
    scanf("%d",&data);

    while(temp!=NULL)
    {
       if(temp->data==data)
       {
	   printf("%d Found at %d\n",data,pos+1);
	   return;
       }
       temp=temp->link;
       pos++;
    }
    printf("\nNot Found\n");

  }

  void reverse()
  {
     struct node *p1,*p2;
     char p;

     p1=root;
     while(p1->link!=NULL)
     {
	p2=p1->link;

	while(p2!=NULL)
	{
	   p=p1->data;
	   p1->data=p2->data;
	   p2->data=p;
	   p2=p2->link;

	}
	p1=p1->link;
     }
  }



  void sort()
  {
      struct node *p,*q,*t;
      char temp;
      p=t=root;
      if(root==NULL)
	  printf("No Lists\n");
      else
      {

	  while(p->link!=NULL)
	  {
	  q=p->link;

		while(q!=NULL)
		{
			if(p->data > q->data)
			{
				temp = p->data;
				p->data = q->data;
				q->data = temp;

			}
			q=q->link;
		}
		p=p->link;
	  }

      }

      while(t!=NULL)
       {
	   printf("%d --> ",t->data);
	   t=t->link;
       }
  }
