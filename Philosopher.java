package io.dama.par.dining.cond;

import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;

import io.dama.par.dining.cond.PhilosopherExperiment;


public class Philosopher extends Thread implements IPhilosopher {
	
	private IPhilosopher left;
	private IPhilosopher right;
	private Lock table;
	private volatile boolean stop;
    private Condition notEating;
    private boolean eating = false;
    private Random random = ThreadLocalRandom.current();

    public Condition getCondition() {
    	return this.notEating;
    }
    
    @Override
    public void setLeft(final IPhilosopher left) {
        this.left = left;

    }

    @Override
    public void setRight(final IPhilosopher right) {
        this.right = right;

    }

    @Override
    public void setTable(final Lock table) {
        this.table = table;
        notEating = table.newCondition();
    }

    @Override
    public void stopPhilosopher() {
    	 System.out.println(getId() + " stopping");
         this.stop = true;
         interrupt();

    }
    
    @Override
    public void start() {
    	
    	super.start();
    }
    
    @Override
    public void run() {
    	System.out.println(Thread.currentThread().getId() + " starting");
    	try {
            while (!this.stop) {
                think();
                eat();
            }
        } catch (final InterruptedException e) {
        }
    	System.out.println(Thread.currentThread().getId() + " stopped");
    }
    
    private void think() throws InterruptedException {
    	table.lock();
    	notEating.signalAll();
    	table.unlock();
    	Thread.sleep(PhilosopherExperiment.MAX_THINKING_DURATION_MS);
    }
    
    private void eat() throws InterruptedException {
    	System.out.println(Thread.currentThread().getId() + " try acquiring table...");
    	table.lock();
    	try {
    		while(((Philosopher)left).isEating() || ((Philosopher)right).isEating()){
    			((Philosopher)left).getCondition().await();
    			((Philosopher)right).getCondition().await();
    		}
    		eating = true;
    		System.out.println(Thread.currentThread().getId() + " eating");
    		table.unlock();
    		try {
    		Thread.sleep(PhilosopherExperiment.MAX_EATING_DURATION_MS);
    		} catch (InterruptedException e){   			
    		}
    		table.lock();
    		System.out.println(Thread.currentThread().getId() + " eaten");
    		eating = false;
    		notEating.signalAll();
    	} finally {
    		table.unlock();
    	}
    	
    }
    
    public boolean isEating() {
    	return eating;
    }
}
